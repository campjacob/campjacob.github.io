#!/usr/bin/env python3
"""
tag-cloud.py — lay out the blog's tags as word clouds, saved as SVG includes.

Writes two files, both plain SVG that Jekyll pastes into the page:
  _includes/tag-cloud.svg          /tags/ page: tags on 3+ posts, each word a link to its tag
  _includes/tag-cloud-sidebar.svg  blog sidebar: the 25 most used tags, small, no links

The layout is worked out here, once, so the browser only has to draw it. (Laying the words
out in the browser froze the page in Safari.) The same seed is used every run, so the
files only change when the tags do.

Usage (from the repo root):
  python3 scripts/tag-cloud.py

It also runs from .github/workflows/tag-cloud.yml whenever _posts/ changes, which commits the
new SVGs and asks GitHub Pages to rebuild. Pull before your next push.

Requirements:
  - pip install wordcloud pyyaml
  - Words are measured with scripts/fonts/Inter-Bold.ttf (Latin only; SIL Open Font License).
    The page shows them in the site's own system font, so each word gets textLength, which
    stretches or squeezes it to the measured width and keeps words from overlapping.
  - Colors come from the page's CSS (.tc-1 to .tc-4), so light and dark mode both work.
  - Links point to #<slug>, using the same rule as Jekyll's slugify, so they match the
    anchors on /tags/. Tags in the posts' `tags:` field only; categories are separate.
"""
import re
import sys
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import yaml
from PIL import Image, ImageFont
from wordcloud import WordCloud

ROOT = Path(__file__).resolve().parent.parent
FONT = str(ROOT / "scripts/fonts/Inter-Bold.ttf")
SEED = 7

CLOUDS = [
    # file, minimum posts, most tags, width, height, largest font, vertical share, links
    dict(out="_includes/tag-cloud.svg", min_posts=3, limit=None, width=1100, height=520,
         max_font=110, vertical=0.35, links=True, label="Tag cloud"),
    dict(out="_includes/tag-cloud-sidebar.svg", min_posts=1, limit=25, width=360, height=300,
         max_font=52, vertical=0.25, links=False, label="Most used tags"),
]


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"warning: {path}: {e}", file=sys.stderr)
        return {}


def slugify(s):
    """Jekyll's default slugify: runs of anything but letters and digits become one hyphen."""
    return re.sub(r"[^0-9a-zÀ-￿]+", "-", s.lower()).strip("-")


def tier(count, most):
    """1 (smallest) to 4 (most used), for the color classes."""
    r = (count / most) ** 0.5
    return 4 if r > 0.75 else 3 if r > 0.45 else 2 if r > 0.25 else 1


def build(counts, c):
    tags = [(t, n) for t, n in counts.most_common() if n >= c["min_posts"]]
    if c["limit"]:
        tags = tags[: c["limit"]]
    freqs = dict(tags)
    most = max(freqs.values())

    wc = WordCloud(font_path=FONT, width=c["width"], height=c["height"], mode="RGBA",
                   background_color=None, prefer_horizontal=1 - c["vertical"],
                   max_font_size=c["max_font"], min_font_size=10, relative_scaling=0.55,
                   margin=4, random_state=SEED, max_words=len(freqs))
    wc.generate_from_frequencies(freqs)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {c["width"]} {c["height"]}" '
           f'class="tag-cloud-svg" role="{"group" if c["links"] else "img"}" '
           f'aria-label="{c["label"]}">']
    if not c["links"]:
        out.append(f"<title>{c['label']}: " + ", ".join(escape(t) for t, _ in tags) + "</title>")
    placed = 0
    for (word, _), size, (y, x), orientation, _ in wc.layout_:
        font = ImageFont.truetype(FONT, size)
        (_, _), (off_x, off_y) = font.font.getsize(word)
        ascent, _ = font.getmetrics()
        length = font.getlength(word)
        if orientation == Image.ROTATE_90:
            # wordcloud turns these counterclockwise, so they read bottom to top.
            tx, ty = x + ascent - off_y, y + length - off_x
            transform = f"translate({tx:.1f},{ty:.1f}) rotate(-90)"
        else:
            transform = f"translate({x - off_x:.1f},{y + ascent - off_y:.1f})"
        n = counts[word]
        text = (f'<text transform="{transform}" font-size="{size}" textLength="{length:.1f}" '
                f'lengthAdjust="spacingAndGlyphs" class="tc-{tier(n, most)}">{escape(word)}</text>')
        if c["links"]:
            posts = f"{n} post" + ("" if n == 1 else "s")
            text = (f'<a href="#{slugify(word)}" data-tag="{slugify(word)}" '
                    f'aria-label={quoteattr(f"{word}, {posts}")}><title>{escape(posts)}</title>{text}</a>')
        out.append(text)
        placed += 1
    out.append("</svg>")

    (ROOT / c["out"]).write_text("\n".join(out) + "\n", encoding="utf-8")
    missing = len(freqs) - placed
    print(f'{c["out"]}: {placed} tags' + (f" ({missing} did not fit)" if missing else ""))


def main():
    counts = Counter()
    for path in sorted((ROOT / "_posts").rglob("*")):
        if path.suffix in (".md", ".markdown", ".html"):
            for t in front_matter(path).get("tags") or []:
                counts[str(t).strip()] += 1
    for c in CLOUDS:
        build(counts, c)


if __name__ == "__main__":
    main()
