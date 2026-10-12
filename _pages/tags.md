---
title: Tags
layout: foundation
nav_group: blog
permalink: /tags/
---
{%- comment -%}
Tags shown three ways: a word cloud of the tags on 3+ posts (the default), or as pills (bigger for more posts)
sorted Most used or A–Z. The cloud is _includes/tag-cloud.svg, laid out by scripts/tag-cloud.py
(a GitHub Action reruns it when posts change). The filter box only shows with the pills, since the cloud can't be filtered.
The chosen tag shows as a chip with an × at the end of the toolbar; it, or clicking the tag again, clears it.
Tags used once are tucked behind a button, but the filter searches them too.
Choosing a tag shows its posts down the same timeline as Posts by Date.
Anchors (#social-work, ...) are the slugs the old theme linked to from each post, so those links still open the right tag.
Without JavaScript every tag's posts are shown, one after another.
{%- endcomment -%}
{%- assign all_tags = "" | split: "" -%}
{%- for p in site.posts -%}{%- for t in p.tags -%}{%- assign all_tags = all_tags | push: t -%}{%- endfor -%}{%- endfor -%}
{%- assign all_tags = all_tags | uniq | sort_natural -%}
{%- assign most = 0 -%}{%- assign once = 0 -%}
{%- for t in all_tags -%}
  {%- assign n = site.posts | where_exp: "p", "p.tags contains t" | size -%}
  {%- if n > most -%}{%- assign most = n -%}{%- endif -%}
  {%- if n == 1 -%}{%- assign once = once | plus: 1 -%}{%- endif -%}
{%- endfor -%}

<article class="tags-index">

<header class="my-4">
  {% include blog-views.htm %}
  <h1 class="fw-bolder">Tags</h1>
  <p class="lead mb-1">I tag my blog posts with the people, places, projects, and topics in them. Click a tag, and it will display all of the posts with that tag.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-tags" aria-hidden="true"></i> {{ all_tags | size }} tags across {{ site.posts | size }} posts.</p>
</header>

<div id="tag-picker" class="mb-4">
  <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
    <div class="btn-group btn-group-sm" role="group" aria-label="Show tags as">
      <button type="button" class="btn btn-outline-secondary active" data-sort="cloud" aria-pressed="true">Cloud</button>
      <button type="button" class="btn btn-outline-secondary" data-sort="count" aria-pressed="false">Most used</button>
      <button type="button" class="btn btn-outline-secondary" data-sort="name" aria-pressed="false">A–Z</button>
    </div>
    <div id="tag-search" class="input-group input-group-sm tag-search d-none">
      <span class="input-group-text"><i class="fas fa-search" aria-hidden="true"></i></span>
      <input type="search" id="tag-filter" class="form-control" placeholder="Filter tags" aria-label="Filter tags" autocomplete="off">
    </div>
    <span id="tag-none" class="small text-body-secondary" hidden>No tags match.</span>
    <button type="button" id="tag-clear" class="tag-pill is-active ms-auto d-none" title="Clear the selected tag"><span id="tag-clear-label"></span><i class="fas fa-times" aria-hidden="true"></i><span class="visually-hidden">Clear the selected tag</span></button>
  </div>

  <div id="tag-wordcloud" class="tag-wordcloud mb-2">{% include tag-cloud.svg %}</div>
  <div class="tag-cloud d-flex flex-wrap gap-2" role="tablist" aria-label="Tags">
    {%- for t in all_tags -%}
    {%- assign n = site.posts | where_exp: "p", "p.tags contains t" | size -%}
    {%- assign w = n | times: 1.0 | divided_by: most | sqrt | round: 2 %}
    <a href="#{{ t | slugify }}" class="tag-pill{% if n == 1 %} is-once{% endif %}" role="tab" id="tab-{{ t | slugify }}" aria-controls="{{ t | slugify }}" aria-selected="false" data-tag="{{ t | slugify }}" data-name="{{ t | downcase | escape }}" data-count="{{ n }}" data-label="{{ t | escape }}" title="{{ n }} {% if n == 1 %}post{% else %}posts{% endif %}" style="--w: {{ w }};">{{ t | escape }} <span class="tag-pill-count">{{ n }}</span></a>
    {%- endfor %}
  </div>
  {%- if once > 0 %}
  <button type="button" id="tag-more" class="btn btn-link btn-sm px-0 mt-2" hidden aria-expanded="false">Show the {{ once }} tags used once</button>
  {%- endif %}
</div>

<p id="tag-prompt" class="text-body-secondary" hidden>Choose a tag to see its posts.</p>

{%- for t in all_tags %}
{%- assign posts = site.posts | where_exp: "p", "p.tags contains t" -%}
{%- assign by_year = posts | group_by_exp: "p", "p.date | date: '%Y'" %}
<section id="{{ t | slugify }}" class="tag-panel mb-5" role="tabpanel" aria-labelledby="tab-{{ t | slugify }}">
  <div class="d-flex align-items-baseline flex-wrap gap-2 mb-3">
    <h2 class="h4 fw-bold mb-0"><i class="fas fa-tag me-2 cat-icon" aria-hidden="true"></i>{{ t | escape }} <span class="small fw-normal text-body-secondary">{{ posts.size }} {% if posts.size == 1 %}post{% else %}posts{% endif %}</span></h2>
    <a href="#tag-picker" class="ms-auto small text-body-secondary text-decoration-none">Back to tags &uarr;</a>
  </div>
  <div class="post-timeline">
  {%- for g in by_year %}
    <section class="year-section">
      <div class="year-section-head d-flex align-items-baseline mb-2">
        <h3 class="h5 fw-bold mb-0">{{ g.name }}</h3>
        <span class="small text-body-secondary ms-2">{{ g.size }} {% if g.size == 1 %}post{% else %}posts{% endif %}</span>
      </div>
      <ul class="list-unstyled mb-0">
        {%- for p in g.items %}
        <li class="date-row">
          <time class="date-row-day text-body-secondary small text-nowrap" datetime="{{ p.date | date: '%Y-%m-%d' }}">{{ p.date | date: "%b %-d" }}</time>
          <div class="date-row-body">
            <a href="{{ p.url | relative_url }}" class="date-row-title">{{ p.title | escape }}</a>
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
</section>
{%- endfor %}

</article>

<script>
// Tag picker: cloud or pills, filter, show the tags used once, and show one tag's posts at a time.
(function () {
  var list = document.querySelector(".tag-cloud");
  var pills = Array.prototype.slice.call(list.querySelectorAll(".tag-pill"));
  var wc = document.getElementById("tag-wordcloud");
  var words = wc.querySelectorAll("[data-tag]");
  var panels = document.querySelectorAll(".tag-panel");
  var filter = document.getElementById("tag-filter");
  var more = document.getElementById("tag-more");
  var none = document.getElementById("tag-none");
  var prompt = document.getElementById("tag-prompt");
  var search = document.getElementById("tag-search");
  var clear = document.getElementById("tag-clear");
  var clearLabel = document.getElementById("tag-clear-label");
  var showOnce = false, view = "cloud", current = "";

  function wanted(p) {
    var q = filter.value.trim().toLowerCase();
    return q ? p.dataset.name.indexOf(q) !== -1
             : showOnce || !p.classList.contains("is-once") || p.dataset.tag === current;
  }

  function refresh() {
    var isCloud = view === "cloud";
    if (isCloud) filter.value = "";
    search.classList.toggle("d-none", isCloud);
    wc.hidden = !isCloud;
    list.classList.toggle("d-none", isCloud);
    if (more) more.hidden = isCloud || !!filter.value.trim();
    var shown = 0;
    pills.forEach(function (p) { p.hidden = !wanted(p); if (!p.hidden) shown++; });
    none.hidden = isCloud || shown > 0;
  }

  function sort(by) {
    view = by;
    if (by !== "cloud") {
      pills.slice().sort(function (a, b) {
        return by === "name" ? a.dataset.name.localeCompare(b.dataset.name)
                             : (b.dataset.count - a.dataset.count) || a.dataset.name.localeCompare(b.dataset.name);
      }).forEach(function (p) { list.appendChild(p); });
    }
    document.querySelectorAll("[data-sort]").forEach(function (b) {
      var on = b.dataset.sort === by;
      b.classList.toggle("active", on);
      b.setAttribute("aria-pressed", on);
    });
    refresh();
  }

  function show(id, scroll) {
    var panel = id && document.getElementById(id);
    if (!panel || !panel.classList.contains("tag-panel")) panel = null;
    current = panel ? id : "";
    pills.forEach(function (p) {
      var on = p.dataset.tag === current;
      p.classList.toggle("is-active", on);
      p.setAttribute("aria-selected", on);
    });
    words.forEach(function (w) { w.classList.toggle("is-active", w.dataset.tag === current); });
    panels.forEach(function (p) { p.hidden = p !== panel; });
    prompt.hidden = !!panel;
    clear.classList.toggle("d-none", !panel);
    clearLabel.textContent = panel ? document.getElementById("tab-" + current).dataset.label : "";
    refresh();
    if (panel && scroll) panel.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function pick(e) {
    e.preventDefault();
    var tag = e.currentTarget.dataset.tag;
    if (tag === current) return deselect();
    history.replaceState(null, "", "#" + tag);
    show(tag, true);
  }

  function deselect() {
    history.replaceState(null, "", location.pathname + location.search);
    show("", false);
  }

  pills.forEach(function (p) { p.addEventListener("click", pick); });
  clear.addEventListener("click", deselect);
  words.forEach(function (w) { w.addEventListener("click", pick); });
  document.querySelectorAll("[data-sort]").forEach(function (b) {
    b.addEventListener("click", function () { sort(b.dataset.sort); });
  });
  filter.addEventListener("input", refresh);
  if (more) {
    var moreLabel = more.textContent;
    more.addEventListener("click", function () {
      showOnce = !showOnce;
      more.setAttribute("aria-expanded", showOnce);
      more.textContent = showOnce ? "Hide the tags used once" : moreLabel;
      refresh();
    });
  }
  window.addEventListener("hashchange", function () { show(location.hash.slice(1), true); });

  sort(view);
  show(location.hash.slice(1), location.hash.length > 1);
})();
</script>
