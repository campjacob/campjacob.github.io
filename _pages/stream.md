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
  collection (presentations' pages here just redirect to the deck), plus blog posts and
  dictionary words straight from their collections. The old Twitter
  microposts are on /stream/archive/. Items render without embeds so they also work in email.
{%- endcomment -%}
{%- comment -%}
  Blog posts and dictionary words join the stream straight from their collections (they get
  `source` from _config.yml defaults). Words are dated by added_to_project, not `date`, so
  they're kept in their own list and merged in by date below. Undated words are left out.
{%- endcomment -%}
{%- assign posts = site.stream | concat: site.posts | sort: "date" | reverse -%}
{%- comment -%} added_to_project is a Date in some entries and a string in others, so sort on "YYYY-MM-DD|path" text {%- endcomment -%}
{%- assign word_keys = "" | split: "" -%}
{%- for w in site.dictionary -%}
  {%- comment -%} only real YYYY-MM-DD values ("date" turns other text into today's date) {%- endcomment -%}
  {%- assign raw = w.added_to_project | append: "" -%}
  {%- assign raw_year = raw | slice: 0, 4 | plus: 0 -%}
  {%- assign wd = w.added_to_project | date: "%Y-%m-%d" -%}
  {%- if raw.size == 10 and raw_year > 1900 -%}{%- assign key = wd | append: "|" | append: w.path -%}{%- assign word_keys = word_keys | push: key -%}{%- endif -%}
{%- endfor -%}
{%- assign word_keys = word_keys | sort | reverse -%}
{%- assign words = "" | split: "" -%}
{%- for k in word_keys -%}
  {%- assign k_path = k | split: "|" | last -%}
  {%- assign w = site.dictionary | where: "path", k_path | first -%}
  {%- assign words = words | push: w -%}
{%- endfor -%}
{%- assign by_source = posts | concat: words | group_by: "source" -%}
{%- assign total = posts.size | plus: words.size -%}
{%- assign page_size = 20 -%}

<div class="stream my-4" style="max-width: 42rem;">

<header class="mb-4">
  <h1 class="fw-bolder">Stream</h1>
  <p class="lead mb-2">I like the <a href="https://indieweb.org/why">IndieWeb</a> idea of owning my own data and having my website be the place that links to everything I do. This is everything I post, here and on other sites (blog posts, presentations, new words, notes, photos, videos, and workouts), gathered in one place.</p>
  <p class="small mb-0">
    <a href="https://social.vsp.ink/@Jacob" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-mastodon fa-fw" aria-hidden="true"></i>Mastodon</a>
    <a href="https://media.vsp.ink/photos" rel="me noopener" class="me-3 text-nowrap"><i class="fas fa-camera-retro fa-fw" aria-hidden="true"></i>Pixelfed</a>
    <a href="https://www.youtube.com/@JacobCampbell82" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-youtube fa-fw" aria-hidden="true"></i>YouTube</a>
    <a href="https://www.tiktok.com/@campjacob1982" rel="me noopener" class="me-3 text-nowrap"><i class="fab fa-tiktok fa-fw" aria-hidden="true"></i>TikTok</a>
    <a href="https://presentations.jacobrcampbell.com/" class="me-3 text-nowrap"><i class="fas fa-person-chalkboard fa-fw" aria-hidden="true"></i>Presentations</a>
    <a href="https://fitpub.social/@campjacob" rel="me noopener" class="text-nowrap"><i class="fas fa-person-running fa-fw" aria-hidden="true"></i>FitPub</a>
  </p>
</header>

<div class="d-flex flex-wrap align-items-center gap-2 mb-3">
  <div class="d-flex flex-wrap gap-1" role="group" aria-label="Filter by site" id="stream-filters">
    <button type="button" class="btn btn-sm btn-outline-primary active" data-filter="all">All <span class="badge text-bg-secondary">{{ total }}</span></button>
    {%- for s in by_source -%}
    {%- case s.name -%}
      {%- when "youtube" -%}{%- assign s_label = "YouTube" -%}
      {%- when "tiktok" -%}{%- assign s_label = "TikTok" -%}
      {%- when "fitpub" -%}{%- assign s_label = "FitPub" -%}
      {%- when "blog" -%}{%- assign s_label = "Blog" -%}
      {%- when "presentations" -%}{%- assign s_label = "Presentations" -%}
      {%- when "dictionary" -%}{%- assign s_label = "Dictionary" -%}
      {%- else -%}{%- assign s_label = s.name | capitalize -%}
    {%- endcase -%}
    <button type="button" class="btn btn-sm btn-outline-primary" data-filter="{{ s.name }}">{{ s_label }} <span class="badge text-bg-secondary">{{ s.items | size }}</span></button>
    {%- endfor -%}
  </div>
  <select class="form-select form-select-sm w-auto ms-sm-auto" id="stream-year" aria-label="Filter by year">
    <option value="all">All years</option>
  </select>
</div>

<div id="stream-list">
{%- assign last_year = "" -%}
{%- assign wi = 0 -%}
{%- comment -%} Not "p": stream-card.htm assigns p, and a loop variable of the same name would shadow it {%- endcomment -%}
{%- for item in posts -%}
  {%- assign pd = item.date | date: "%Y-%m-%d" -%}
  {%- for w in words offset: wi -%}
    {%- assign wd = w.added_to_project | date: "%Y-%m-%d" -%}
    {%- if wd < pd -%}{%- break -%}{%- endif -%}
    {%- assign wi = wi | plus: 1 -%}
    {% include stream-row.htm post=w date=w.added_to_project %}
  {%- endfor -%}
  {% include stream-row.htm post=item date=item.date %}
{%- endfor -%}
{%- for w in words offset: wi -%}
  {% include stream-row.htm post=w date=w.added_to_project %}
{%- endfor -%}
</div>

<div class="text-center my-4">
  <button type="button" class="btn btn-outline-primary d-none" id="stream-more">Show more</button>
</div>

<p class="text-body-secondary small border-top pt-3"><i class="fas fa-archive" aria-hidden="true"></i> Looking for my older Twitter posts? They're in the <a href="/stream/archive/">stream archive</a>.</p>

</div>

<script>
// Filter by site and year, showing {{ page_size }} at a time. Without JS everything shows.
(function () {
  var size = {{ page_size }}, shown = size, filter = "all", year = "all";
  var list = document.getElementById("stream-list");
  var cards = Array.prototype.slice.call(list.querySelectorAll(".stream-item"));
  var more = document.getElementById("stream-more");
  var yearSelect = document.getElementById("stream-year");
  var filters = document.getElementById("stream-filters");
  function render() {
    var matching = cards.filter(function (c) {
      return (filter === "all" || c.dataset.source === filter) && (year === "all" || c.dataset.year === year);
    });
    cards.forEach(function (c) { c.classList.add("d-none"); });
    matching.slice(0, shown).forEach(function (c) { c.classList.remove("d-none"); });
    list.querySelectorAll(".stream-year").forEach(function (h) {
      var el = h.nextElementSibling, any = false;
      while (el && !el.classList.contains("stream-year")) { if (!el.classList.contains("d-none")) any = true; el = el.nextElementSibling; }
      h.classList.toggle("d-none", !any);
    });
    more.classList.toggle("d-none", matching.length <= shown);
    more.textContent = "Show more (" + (matching.length - Math.min(shown, matching.length)) + " left)";
  }
  filters.querySelectorAll("[data-filter]").forEach(function (b) {
    b.addEventListener("click", function () {
      filters.querySelectorAll(".active").forEach(function (a) { a.classList.remove("active"); });
      b.classList.add("active"); filter = b.dataset.filter; shown = size; render();
    });
  });
  var years = [], counts = {};
  cards.forEach(function (c) { var y = c.dataset.year; if (!counts[y]) { counts[y] = 0; years.push(y); } counts[y]++; });
  years.sort().reverse().forEach(function (y) {
    var o = document.createElement("option"); o.value = y; o.textContent = y + " (" + counts[y] + ")"; yearSelect.appendChild(o);
  });
  yearSelect.addEventListener("change", function () { year = yearSelect.value; shown = size; render(); });
  more.addEventListener("click", function () { shown += size; render(); });
  render();
})();
</script>
