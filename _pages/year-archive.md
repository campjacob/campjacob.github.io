---
title: Posts by Date
layout: foundation
nav_group: blog
permalink: /year-archive/
---
{%- comment -%} Every post, newest first, grouped by year along a vertical timeline. The horizontal timeline at the top has a dot and stem per year (both bigger for more posts, empty years hollow); it scrolls sideways and opens on the newest years. {%- endcomment -%}
{%- assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" -%}
{%- assign newest = site.posts | first -%}
{%- assign oldest = site.posts | last -%}
{%- assign first_year = oldest.date | date: "%Y" | plus: 0 -%}
{%- assign last_year = newest.date | date: "%Y" | plus: 0 -%}
{%- assign most = 0 -%}
{%- for g in by_year -%}{%- if g.size > most -%}{%- assign most = g.size -%}{%- endif -%}{%- endfor -%}

<article class="date-archive">

<header class="my-4">
  {% include blog-views.htm %}
  <h1 class="fw-bolder">Posts by Date</h1>
  <p class="lead mb-1">All of my blog posts, newest first. Choose a year on the timeline to jump to it.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-calendar-alt" aria-hidden="true"></i> {{ site.posts | size }} posts from {{ first_year }} to {{ last_year }}.</p>
</header>

<nav class="tl mb-5" aria-labelledby="timeline-title">
  <h2 id="timeline-title" class="h6 fw-bold text-body-secondary text-uppercase mb-2">Timeline</h2>
  <div class="tl-frame">
    <button type="button" class="tl-arrow tl-prev btn btn-sm btn-outline-secondary rounded-circle" aria-label="Earlier years"><i class="fas fa-chevron-left" aria-hidden="true"></i></button>
    <div class="tl-scroll" tabindex="0" aria-label="Years, scroll sideways for more">
      <ol class="tl-track list-unstyled mb-0">
        {%- for y in (first_year..last_year) -%}
        {%- assign ys = y | append: "" -%}
        {%- assign g = by_year | where: "name", ys | first -%}
        {%- assign n = g.size | default: 0 -%}
        {%- assign side = forloop.index | modulo: 2 -%}
        {%- comment -%} Stem length grows with the post count (square root, so busy years don't dwarf the rest). {%- endcomment -%}
        {%- assign stem = n | times: 1.0 | divided_by: most | sqrt | times: 52 | plus: 18 | round -%}
        {%- assign dot = n | times: 1.0 | divided_by: most | sqrt | times: 18 | plus: 10 | round -%}
        {%- comment -%} A standing note on some years only: many countries, or a busy year. Others show their count on hover. {%- endcomment -%}
        {%- assign y_countries = "" | split: "" -%}
        {%- for p in g.items -%}{%- for key in p.locations -%}{%- assign c = site.data.locations[key].country -%}{%- if c -%}{%- assign y_countries = y_countries | push: c -%}{%- endif -%}{%- endfor -%}{%- endfor -%}
        {%- assign c_count = y_countries | uniq | size -%}
        {%- if c_count >= 3 -%}{%- assign note = c_count | append: " countries" -%}{%- assign loud = true -%}
        {%- elsif n >= 18 -%}{%- assign note = n | append: " posts" -%}{%- assign loud = true -%}
        {%- else -%}{%- capture note %}{{ n }} {% if n == 1 %}post{% else %}posts{% endif %}{% endcapture -%}{%- assign loud = false -%}{%- endif %}
        <li class="tl-year {% if side == 1 %}is-up{% else %}is-down{% endif %}{% if n == 0 %} is-empty{% endif %}" style="--stem: {{ stem }}px; --dot: {{ dot }}px;">
          {%- if n > 0 %}
          <a href="#y-{{ y }}" class="tl-hit" aria-label="{{ y }}: {{ n }} {% if n == 1 %}post{% else %}posts{% endif %}{% if c_count > 1 %} from {{ c_count }} countries{% endif %}">
            <span class="tl-stem"></span><span class="tl-tip"></span>
            <span class="tl-note{% unless loud %} is-quiet{% endunless %}" aria-hidden="true">{{ note }}</span>
            <span class="tl-label" aria-hidden="true">{{ y }}</span>
          </a>
          {%- else %}
          <span class="tl-hit" title="{{ y }}: no posts"><span class="tl-label">{{ y }}</span></span>
          {%- endif %}
        </li>
        {%- endfor %}
      </ol>
    </div>
    <button type="button" class="tl-arrow tl-next btn btn-sm btn-outline-secondary rounded-circle" aria-label="Later years"><i class="fas fa-chevron-right" aria-hidden="true"></i></button>
  </div>
</nav>

<div class="post-timeline">
{%- for g in by_year %}
<section id="y-{{ g.name }}" class="year-section">
  <div class="year-section-head d-flex align-items-baseline mb-2">
    <h2 class="h4 fw-bold mb-0">{{ g.name }}</h2>
    <span class="small text-body-secondary ms-2">{{ g.size }} {% if g.size == 1 %}post{% else %}posts{% endif %}</span>
    <a href="#timeline-title" class="ms-auto small text-body-secondary text-decoration-none">Back to timeline &uarr;</a>
  </div>
  <ul class="list-unstyled mb-0">
    {%- for p in g.items -%}
    {%- assign kind = "" -%}
    {%- if p.categories contains "Link Post" -%}{%- assign kind = "Link" -%}
    {%- elsif p.categories contains "YouTube Videos" -%}{%- assign kind = "Video" -%}
    {%- elsif p.categories contains "Travel Blog" -%}{%- assign kind = "Travel" -%}
    {%- elsif p.categories contains "Professional Blog" -%}{%- assign kind = "Professional" -%}
    {%- elsif p.categories contains "Personal Blog" -%}{%- assign kind = "Personal" -%}{%- endif %}
    <li class="date-row">
      <time class="date-row-day text-body-secondary small text-nowrap" datetime="{{ p.date | date: '%Y-%m-%d' }}">{{ p.date | date: "%b %-d" }}</time>
      <div class="date-row-body">
        <a href="{{ p.url | relative_url }}" class="date-row-title">{{ p.title | escape }}</a>
        {%- if kind != "" %} <span class="badge text-bg-light border fw-normal">{{ kind }}</span>{% endif %}
        {%- if p.locations.size > 0 %}
        {%- assign first_place = p.locations | first -%}
        {%- assign place = site.data.locations[first_place].place | default: first_place %} <a href="{{ '/locations/' | relative_url }}#l-{{ first_place | slugify }}" class="date-row-place small text-body-secondary text-decoration-none text-nowrap"><i class="fas fa-map-pin me-1" aria-hidden="true"></i>{{ place }}{% if p.locations.size > 1 %} +{{ p.locations.size | minus: 1 }}{% endif %}</a>
        {%- endif %}
      </div>
    </li>
    {%- endfor %}
  </ul>
</section>
{%- endfor %}
</div>

</article>

<script>
// Year timeline: open on the newest years, and step sideways with the arrows.
(function () {
  var scroller = document.querySelector(".tl-scroll");
  if (!scroller) return;
  var prev = document.querySelector(".tl-prev"), next = document.querySelector(".tl-next");
  function update() {
    var max = scroller.scrollWidth - scroller.clientWidth;
    var none = max <= 1;
    prev.hidden = next.hidden = none;
    prev.disabled = scroller.scrollLeft <= 1;
    next.disabled = scroller.scrollLeft >= max - 1;
  }
  function step(dir) { scroller.scrollBy({ left: dir * scroller.clientWidth * 0.8, behavior: "smooth" }); }
  prev.addEventListener("click", function () { step(-1); });
  next.addEventListener("click", function () { step(1); });
  scroller.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  scroller.style.scrollBehavior = "auto";
  scroller.scrollLeft = scroller.scrollWidth;
  scroller.style.scrollBehavior = "";
  update();
})();
</script>
