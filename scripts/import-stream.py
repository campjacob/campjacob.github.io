#!/usr/bin/env python3
"""
import-stream.py — pull my posts from other services into the /stream/ section (PESOS).

Each post becomes one file:  _stream/<source>/YYYY-MM-DD-<source>-<id>.md
Files that already exist are left alone, so re-running only adds new posts. The same
script does the one-time backfill and the scheduled GitHub Action.

Sources and what they become (the `kind` field):
  mastodon  @Jacob@social.vsp.ink      note
  pixelfed  @photos@media.vsp.ink      photo
  youtube   @JacobCampbell82           video
  tiktok    @campjacob1982             video
  fitpub    @campjacob@fitpub.social   activity

Usage (from the repo root):
  python3 scripts/import-stream.py all                # everything new, every source
  python3 scripts/import-stream.py all --dry-run      # report only
  python3 scripts/import-stream.py youtube --limit 3  # first few, for testing

It also runs every few hours from .github/workflows/import-stream.yml, which commits new
posts and asks GitHub Pages to rebuild (pushes made by the Action don't trigger a build).

Requirements:
  - Pixelfed's API needs a token (read scope), from $PIXELFED_TOKEN or, on the Mac, the
    Keychain item "pixelfed-token":
      security add-generic-password -U -a "$USER" -s pixelfed-token -w "$(pbpaste)"
    Tokens come from media.vsp.ink Settings > Applications. If "Create" does nothing, the
    server needs `php artisan passport:client --personal --provider=users` once.
  - FitPub has no tokens or public list API. Its activities are found through social.vsp.ink,
    which follows @campjacob@fitpub.social and keeps public copies of what it receives (so
    only activities federated after the follow appear). Each one's details and route-map
    image come from FitPub's public /api/activities/<id>.
  - YouTube and TikTok are read with yt-dlp (`yt-dlp` on PATH, else `uvx yt-dlp`). Neither
    has a usable API: YouTube's RSS feed 404s and TikTok has none.

Choices the code can't explain on its own:
  - Media is NOT copied into the repo (it is near the GitHub Pages 1 GB cap). Posts point at
    my own servers or stable CDN URLs, and plain <img> works in email newsletters. TikTok is
    the exception: its thumbnail URLs expire, so a small JPEG goes to
    assets/media/stream/tiktok/.
  - Skipped: replies (including self-replies in threads) and boosts. A boost of my own Pixelfed
    or FitPub post is recorded as a cross-post instead (see below).
  - Cross-posts (a Mastodon post linking to my Pixelfed post, blog, or site) are imported like
    any other post, and also recorded in _data/stream_crossposts.yml so the original shows an
    "Also on Mastodon" link. That file is rebuilt on every full Mastodon run.
  - Post HTML goes in the content_html front-matter field, not the body, so Liquid and
    Markdown never process it.
Standard library only (plus yt-dlp), so it runs on a stock GitHub Actions runner.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "_stream")
CROSSPOSTS = os.path.join(REPO, "_data", "stream_crossposts.yml")
TIKTOK_THUMBS = os.path.join(REPO, "assets", "media", "stream", "tiktok")
UA = "jacobrcampbell.com stream importer"

FEDIVERSE = {
    "mastodon": {"base": "https://social.vsp.ink", "acct": "Jacob", "label": "Mastodon", "kind": "note"},
    "pixelfed": {"base": "https://media.vsp.ink", "acct": "photos", "label": "Pixelfed", "kind": "photo",
                 "account_id": "794315914761424897", "token": "pixelfed-token"},
}
YTDLP = {
    "youtube": {"url": "https://www.youtube.com/@JacobCampbell82/videos", "label": "YouTube"},
    "tiktok": {"url": "https://www.tiktok.com/@campjacob1982", "label": "TikTok"},
}
FITPUB = {"via": "https://social.vsp.ink", "acct": "campjacob@fitpub.social", "base": "https://fitpub.social"}
SOURCES = [*FEDIVERSE, *YTDLP, "fitpub"]


# ---------------------------------------------------------------- helpers

def get(url, token=None, raw=False):
    headers = {"User-Agent": UA, "Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read() if raw else (json.load(r), r.headers.get("Link", ""))


def plain(html_text):
    """Post HTML -> readable plain text (keeps line breaks)."""
    t = re.sub(r"<br\s*/?>", "\n", html_text or "")
    t = re.sub(r"</p>\s*<p>", "\n\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()


def text_to_html(text):
    """Plain description (YouTube/TikTok) -> paragraphs with links."""
    out = []
    for para in re.split(r"\n\s*\n", (text or "").strip()):
        p = html.escape(para)
        p = re.sub(r"(https?://[^\s<]+)", r'<a href="\1" rel="noopener">\1</a>', p)
        out.append("<p>" + p.replace("\n", "<br>") + "</p>")
    return "".join(o for o in out if o != "<p></p>")


def yq(s):
    """Quote a string for YAML front matter (JSON strings are valid YAML)."""
    return json.dumps(s if s is not None else "", ensure_ascii=False)


def title_from(text, fallback):
    first = (text or "").split("\n")[0].strip()
    return (first[:77] + "…") if len(first) > 78 else (first or fallback)


def write_post(src, created, post_id, fields, args):
    """fields: list of front-matter lines after the common ones."""
    folder = os.path.join(OUT, src)
    name = f"{created.strftime('%Y-%m-%d')}-{src}-{post_id}.md"
    if not args.dry_run:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, name), "w") as f:
            f.write("\n".join(["---", *fields, "---", ""]))


def existing_ids(src):
    folder = os.path.join(OUT, src)
    if not os.path.isdir(folder):
        return set()
    # Names are YYYY-MM-DD-<src>-<id>.md; YouTube and FitPub ids contain dashes themselves.
    prefix = re.compile(rf"^\d{{4}}-\d{{2}}-\d{{2}}-{src}-")
    return {prefix.sub("", f).removesuffix(".md") for f in os.listdir(folder) if f.endswith(".md")}


def report(src, args, c):
    verb = "would add" if args.dry_run else "added"
    extra = ", ".join(f"{v} {k}" for k, v in c.items() if k not in ("new", "exists") and v)
    print(f"{src}: {verb} {c['new']} | already had {c['exists']}" + (f" | skipped {extra}" if extra else ""))


# ---------------------------------------------------------------- fediverse (Mastodon API)

def token_for(src):
    name = FEDIVERSE[src].get("token")
    if not name:
        return None
    env = os.environ.get(name.upper().replace("-", "_"))
    if env:
        return env
    try:
        return subprocess.run(["security", "find-generic-password", "-s", name, "-w"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        raise RuntimeError(f"no token. Set ${name.upper().replace('-', '_')} or add Keychain item '{name}'.")


def statuses(src, token):
    cfg = FEDIVERSE[src]
    acct_id = cfg.get("account_id") or get(f"{cfg['base']}/api/v1/accounts/lookup?acct={cfg['acct']}", token)[0]["id"]
    # Mastodon includes boosts so boosts of my own Pixelfed/FitPub posts count as cross-posts.
    reblogs = "" if src == "mastodon" else "&exclude_reblogs=true"
    first = f"{cfg['base']}/api/v1/accounts/{acct_id}/statuses?limit=40{reblogs}"
    url = first
    while url:
        page, link = get(url, token)
        if not page:
            break
        yield from page
        # Mastodon pages with a Link header; Pixelfed doesn't, so fall back to max_id.
        m = re.search(r'<([^>]+)>; rel="next"', link)
        url = m.group(1) if m else f"{first}&max_id={page[-1]['id']}"


def crosspost_target(src, status):
    """If this Mastodon post shares something of mine published elsewhere, return its key."""
    if src != "mastodon":
        return None
    links = re.findall(r'href="([^"]+)"', status["content"] or "")
    links.append((status.get("card") or {}).get("url") or "")
    for u in links:
        u = html.unescape(u)
        m = re.search(r"media\.vsp\.ink/(?:p/photos|i/web/post)/(\d+)", u)
        if m:
            return f"pixelfed:{m.group(1)}"
        m = re.search(r"//(?:www\.)?jacobrcampbell\.com(/[^?#\s]*)", u)
        if m:
            path = m.group(1) if m.group(1).endswith("/") else m.group(1) + "/"
            return f"site:{path}"
        if "media.vsp.ink" in u or "fitpub.social" in u:
            return "other"
    return None


def fediverse_fields(src, s):
    cfg = FEDIVERSE[src]
    created = dt.datetime.fromisoformat(s["created_at"].replace("Z", "+00:00")).astimezone()
    text = plain(s["content"])
    lines = [
        f"title: {yq(title_from(text, 'Post on ' + cfg['label']))}",
        f"date: {created.strftime('%Y-%m-%d %H:%M:%S %z')}",
        f"source: {src}",
        f"kind: {cfg['kind']}",
        f"post_id: {yq(s['id'])}",
        f"post_url: {yq(s['url'])}",
        f"post_text: {yq(text)}",
        f"content_html: {yq(s['content'] or '')}",
    ]
    tags = [t["name"] for t in s.get("tags", [])]
    if tags:
        lines += ["tags_fediverse:", *[f"  - {yq(t)}" for t in tags]]
    media = [m for m in s.get("media_attachments", []) if m.get("url")]
    if media:
        lines.append("media:")
        for m in media:
            meta = (m.get("meta") or {}).get("original") or {}
            lines += [f"  - type: {yq(m['type'])}",
                      f"    url: {yq(m['url'])}",
                      f"    preview_url: {yq(m.get('preview_url') or m['url'])}",
                      f"    alt: {yq(m.get('description') or '')}"]
            if meta.get("width") and meta.get("height"):
                lines += [f"    width: {meta['width']}", f"    height: {meta['height']}"]
    card = s.get("card")
    if card and card.get("url") and not media:
        lines += ["link_card:",
                  f"  url: {yq(card['url'])}",
                  f"  title: {yq(card.get('title'))}",
                  f"  description: {yq(card.get('description'))}"]
        if card.get("image"):
            lines.append(f"  image: {yq(card['image'])}")
    return created, lines


def run_fediverse(src, args):
    token = token_for(src)
    have = existing_ids(src)
    c = {"new": 0, "exists": 0, "replies": 0, "not public": 0, "boosts": 0}
    n_cross = 0
    crossposts = {}
    for s in statuses(src, token):
        if s.get("reblog"):
            c["boosts"] += 1
            b = s["reblog"]
            m = re.search(r"media\.vsp\.ink/p/photos/(\d+)|fitpub\.social/activities/([0-9a-f-]{36})", b.get("url") or "")
            if m:
                key = f"pixelfed:{m.group(1)}" if m.group(1) else f"fitpub:{m.group(2)}"
                # The boost has no page of its own; link to the boosted post on my instance.
                where = f"{FEDIVERSE[src]['base']}/@{b['account']['acct']}/{b['id']}"
                crossposts.setdefault(key, []).append({"label": FEDIVERSE[src]["label"], "url": where})
                n_cross += 1
            continue
        if s.get("in_reply_to_id"):
            c["replies"] += 1; continue
        if s.get("visibility") not in ("public", "unlisted"):
            c["not public"] += 1; continue
        target = crosspost_target(src, s)
        if target and target != "other":
            n_cross += 1
            crossposts.setdefault(target, []).append({"label": FEDIVERSE[src]["label"], "url": s["url"]})
        if s["id"] in have:
            c["exists"] += 1; continue
        created, lines = fediverse_fields(src, s)
        write_post(src, created, s["id"], lines, args)
        c["new"] += 1
        if args.limit and c["new"] >= args.limit:
            break
    if src == "mastodon" and not args.limit and not args.dry_run:
        write_crossposts(crossposts)
    report(src, args, c)
    if n_cross:
        print(f"  {n_cross} cross-posts recorded for \"Also on\" links")


def write_crossposts(crossposts):
    lines = ["# Written by scripts/import-stream.py; do not edit by hand.",
             "# Key = where the original lives (pixelfed:<id>, site:<path>); value = the cross-posts.",
             "# The stream card and, later, blog posts show these as \"Also on\" links."]
    for key in sorted(crossposts):
        lines.append(f"{yq(key)}:")
        for x in crossposts[key]:
            lines += [f"  - label: {yq(x['label'])}", f"    url: {yq(x['url'])}"]
    with open(CROSSPOSTS, "w") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------- YouTube / TikTok (yt-dlp)

def ytdlp(*args):
    exe = ["yt-dlp"] if shutil.which("yt-dlp") else ["uvx", "yt-dlp"]
    r = subprocess.run([*exe, "--no-warnings", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {r.stderr.strip()[:400]}")
    return [json.loads(line) for line in r.stdout.splitlines() if line.strip()]


def run_ytdlp(src, args):
    cfg = YTDLP[src]
    have = existing_ids(src)
    c = {"new": 0, "exists": 0}
    listing = ytdlp("--flat-playlist", "-j", cfg["url"])
    for item in listing:
        vid = str(item["id"])
        if vid in have:
            c["exists"] += 1; continue
        v = ytdlp("-j", "--skip-download", item.get("url") or item.get("webpage_url"))[0]
        ts = v.get("timestamp") or dt.datetime.strptime(v["upload_date"], "%Y%m%d").timestamp()
        created = dt.datetime.fromtimestamp(ts).astimezone()
        description = v.get("description") or ""
        if src == "youtube":
            title = v.get("title") or "Video on YouTube"
            body = description
            thumb = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
        else:  # TikTok: the caption is the post; its thumbnail URLs expire, so keep a copy.
            title = title_from(description, "Video on TikTok")
            body = description
            thumb = f"/assets/media/stream/tiktok/{vid}.jpg"
            if not args.dry_run:
                os.makedirs(TIKTOK_THUMBS, exist_ok=True)
                with open(os.path.join(TIKTOK_THUMBS, f"{vid}.jpg"), "wb") as f:
                    f.write(get(v["thumbnail"], raw=True))
        lines = [
            f"title: {yq(title)}",
            f"date: {created.strftime('%Y-%m-%d %H:%M:%S %z')}",
            f"source: {src}",
            "kind: video",
            f"post_id: {yq(vid)}",
            f"post_url: {yq(v.get('webpage_url'))}",
            f"post_text: {yq(body)}",
            f"content_html: {yq(text_to_html(body))}",
            "video:",
            f"  thumbnail: {yq(thumb)}",
            f"  duration: {int(v.get('duration') or 0)}",
        ]
        if src == "youtube":
            lines.insert(1, "show_title: true")
        write_post(src, created, vid, lines, args)
        c["new"] += 1
        if args.limit and c["new"] >= args.limit:
            break
    report(src, args, c)


# ---------------------------------------------------------------- FitPub

def run_fitpub(args):
    have = existing_ids("fitpub")
    c = {"new": 0, "exists": 0, "not found": 0}
    acct = get(f"{FITPUB['via']}/api/v1/accounts/lookup?acct={FITPUB['acct']}")[0]
    first = f"{FITPUB['via']}/api/v1/accounts/{acct['id']}/statuses?limit=40"
    url = first
    while url:
        page, link = get(url)
        if not page:
            break
        for s in page:
            m = re.search(r"/activities/([0-9a-f-]{36})", s.get("url") or s.get("uri") or "")
            if not m or s.get("in_reply_to_id"):
                continue
            aid = m.group(1)
            if aid in have:
                c["exists"] += 1; continue
            try:
                a = get(f"{FITPUB['base']}/api/activities/{aid}")[0]
            except urllib.error.HTTPError:
                c["not found"] += 1; continue
            created = dt.datetime.fromisoformat(a["startedAt"].replace("Z", "+00:00")).astimezone()
            desc = (a.get("description") or "").strip()
            lines = [
                f"title: {yq(a.get('title') or 'Activity on FitPub')}",
                "show_title: true",
                f"date: {created.strftime('%Y-%m-%d %H:%M:%S %z')}",
                "source: fitpub",
                "kind: activity",
                f"post_id: {yq(aid)}",
                f"post_url: {yq(FITPUB['base'] + '/activities/' + aid)}",
                f"post_text: {yq(desc)}",
                f"content_html: {yq(text_to_html(desc))}",
                "activity:",
                f"  type: {yq(a.get('activityType'))}",
                f"  distance_m: {round(a.get('totalDistance') or 0)}",
                f"  duration_s: {int(a.get('totalDurationSeconds') or 0)}",
                f"  elevation_m: {round(a.get('elevationGain') or 0)}",
                f"  location: {yq(a.get('activityLocation'))}",
                f"  image: {yq(FITPUB['base'] + '/api/activities/' + aid + '/image')}",
            ]
            write_post("fitpub", created, aid, lines, args)
            c["new"] += 1
            if args.limit and c["new"] >= args.limit:
                url = None; break
        else:
            m = re.search(r'<([^>]+)>; rel="next"', link)
            url = m.group(1) if m else None
    report("fitpub", args, c)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", choices=[*SOURCES, "all"])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    # One source failing (TikTok blocking a datacenter IP, say) doesn't stop the others;
    # the exit code still reports it so the Action shows a warning.
    failed = []
    for src in (SOURCES if args.source == "all" else [args.source]):
        try:
            if src == "fitpub":
                run_fitpub(args)
            else:
                (run_fediverse if src in FEDIVERSE else run_ytdlp)(src, args)
        except Exception as e:  # noqa: BLE001 - report and keep going
            failed.append(src)
            print(f"{src}: FAILED - {e}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
