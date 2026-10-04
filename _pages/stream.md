---
title: Stream
layout: foundation
nav_group: stream
author_sidebar: true
permalink: /stream/
redirect_from:
  - /microposts/
---
{%- comment -%}
  Everything I post elsewhere, imported by scripts/import-stream.py into the _stream
  collection. The old Twitter/TikTok microposts are on /stream/archive/. Items render
  without embeds so they also work in email.
{%- endcomment -%}
{%- assign posts = site.stream | sort: "date" | reverse -%}
{%- assign by_source = posts | group_by: "source" -%}
{%- assign page_size = 20 -%}

<div class="stream my-4" style="max-width: 42rem;">

<header class="mb-4">
  <h1 class="fw-bolder">Stream</h1>
  <p class="lead mb-2">I like the <a href="https://indieweb.org/why">IndieWeb</a> idea of owning my own data and having my website be the place that links to everything I do. This is everything I post on other sites (notes, photos, videos, and workouts), gathered in one place.</p>
  <p class="small mb-0">
    <a href="https://social.vsp.ink/@Jacob" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-mastodon fa-fw" aria-hidden="true"></i>Mastodon</a>
    <a href="https://media.vsp.ink/photos" rel="me noopener" class="me-3 text-nowrap"><i class="fas fa-camera-retro fa-fw" aria-hidden="true"></i>Pixelfed</a>
    <a href="https://www.youtube.com/@JacobCampbell82" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-youtube fa-fw" aria-hidden="true"></i>YouTube</a>
    <a href="https://www.tiktok.com/@campjacob1982" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-tiktok fa-fw" aria-hidden="true"></i>TikTok</a>
    <a href="https://fitpub.social/@campjacob" rel="me noopener" class="text-nowrap"><i class="fas fa-person-running fa-fw" aria-hidden="true"></i>FitPub</a>
  </p>
</header>

{%- if by_source.size > 1 -%}
<div class="d-flex flex-wrap gap-1 mb-3" role="group" aria-label="Filter by site" id="stream-filters">
  <button type="button" class="btn btn-sm btn-outline-primary active" data-filter="all">All <span class="badge text-bg-secondary">{{ posts | size }}</span></button>
  {%- for s in by_source -%}
  {%- case s.name -%}
    {%- when "youtube" -%}{%- assign s_label = "YouTube" -%}
    {%- when "tiktok" -%}{%- assign s_label = "TikTok" -%}
    {%- when "fitpub" -%}{%- assign s_label = "FitPub" -%}
    {%- else -%}{%- assign s_label = s.name | capitalize -%}
  {%- endcase -%}
  <button type="button" class="btn btn-sm btn-outline-primary" data-filter="{{ s.name }}">{{ s_label }} <span class="badge text-bg-secondary">{{ s.items | size }}</span></button>
  {%- endfor -%}
</div>
{%- endif -%}

<div id="stream-list">
{%- assign last_year = "" -%}
{%- for p in posts -%}
  {%- assign y = p.date | date: "%Y" -%}
  {%- if y != last_year -%}
  <h2 class="h6 fw-bold text-body-secondary border-bottom pb-1 mt-4 mb-3 stream-year" data-year="{{ y }}">{{ y }}</h2>
  {%- assign last_year = y -%}
  {%- endif -%}
  {% include stream-card.htm post=p %}
{%- endfor -%}
</div>

<div class="text-center my-4">
  <button type="button" class="btn btn-outline-primary d-none" id="stream-more">Show more</button>
</div>

<p class="text-body-secondary small border-top pt-3"><i class="fas fa-archive" aria-hidden="true"></i> Looking for my older Twitter posts? They're in the <a href="/stream/archive/">stream archive</a>.</p>

</div>

<script>
// Show items {{ page_size }} at a time, with an optional site filter. Without JS everything shows.
(function () {
  var size = {{ page_size }}, shown = size, filter = "all";
  var cards = Array.prototype.slice.call(document.querySelectorAll("#stream-list .stream-item"));
  var years = document.querySelectorAll("#stream-list .stream-year");
  var more = document.getElementById("stream-more");
  function render() {
    var matching = cards.filter(function (c) { return filter === "all" || c.dataset.source === filter; });
    cards.forEach(function (c) { c.classList.add("d-none"); });
    matching.slice(0, shown).forEach(function (c) { c.classList.remove("d-none"); });
    years.forEach(function (h) {
      var el = h.nextElementSibling, any = false;
      while (el && !el.classList.contains("stream-year")) { if (!el.classList.contains("d-none")) any = true; el = el.nextElementSibling; }
      h.classList.toggle("d-none", !any);
    });
    more.classList.toggle("d-none", matching.length <= shown);
    more.textContent = "Show more (" + (matching.length - Math.min(shown, matching.length)) + " left)";
  }
  more.addEventListener("click", function () { shown += size; render(); });
  document.querySelectorAll("#stream-filters [data-filter]").forEach(function (b) {
    b.addEventListener("click", function () {
      document.querySelectorAll("#stream-filters .active").forEach(function (a) { a.classList.remove("active"); });
      b.classList.add("active"); filter = b.dataset.filter; shown = size; render();
    });
  });
  render();
})();
</script>
