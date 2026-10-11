---
title: Categories
layout: foundation
nav_group: blog
permalink: /categories/
---
{%- comment -%}
The blog's categories as cards, with All first (and chosen by default); the chosen one's posts run down the same timeline as Posts by Date.
Under All, each post shows its categories' icons between the date and title.
Anchors (#personal-blog, #travel-blog, ...) are the slugs the old theme linked to from each post, so those links still open the right category.
Without JavaScript every category's posts are shown, one after another.
{%- endcomment -%}
{%- assign cats = "All|fa-layer-group|See all my blog posts, including posts from other categories.;Personal Blog|fa-user|Sharing about my life and all of the things in and around it.;Travel Blog|fa-plane|My experiences going to other places.;Professional Blog|fa-briefcase|Related to social work, education, and my profession.;YouTube Videos|fa-play-circle|Videos I've posted to YouTube.;Link Post|fa-link|Something worth sharing from elsewhere." | split: ";" -%}

<article class="categories-index">

<header class="my-4">
  {% include blog-views.htm %}
  <h1 class="fw-bolder">Categories</h1>
  <p class="lead mb-1">I categorize my blog posts. Click a type of post, and it will display all of the posts in that category.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-folder-open" aria-hidden="true"></i> {{ site.posts | size }} posts in {{ cats | size | minus: 1 }} categories. Some posts are in more than one.</p>
</header>

<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-6 g-3 mb-4" role="tablist" aria-label="Categories">
  {%- for c in cats -%}
  {%- assign parts = c | split: "|" -%}
  {%- assign cat = parts[0] -%}{%- if cat == "All" -%}{%- assign posts = site.posts -%}{%- else -%}{%- assign posts = site.posts | where_exp: "p", "p.categories contains cat" -%}{%- endif -%}
  {%- assign label = parts[0] | remove: " Blog" -%}
  {%- if parts[0] == "Link Post" -%}{%- assign label = "Link Posts" -%}{%- elsif parts[0] == "YouTube Videos" -%}{%- assign label = "Videos" -%}{%- endif %}
  <div class="col">
    <a href="#{{ parts[0] | slugify }}" class="card h-100 shadow-sm text-decoration-none text-body cat-card" role="tab" id="tab-{{ parts[0] | slugify }}" aria-controls="{{ parts[0] | slugify }}" aria-selected="false" data-cat="{{ parts[0] | slugify }}">
      <div class="card-body">
        <div class="d-flex align-items-center mb-2">
          <i class="fas {{ parts[1] }} fa-lg me-2 cat-icon" aria-hidden="true"></i>
          <h2 class="h6 fw-bold mb-0">{{ label }}</h2>
          <span class="badge rounded-pill text-bg-secondary ms-auto">{{ posts.size }}</span>
        </div>
        <p class="small text-body-secondary mb-0">{{ parts[2] }}</p>
      </div>
    </a>
  </div>
  {%- endfor %}
</div>

{%- for c in cats %}
{%- assign parts = c | split: "|" -%}
{%- assign cat = parts[0] -%}{%- if cat == "All" -%}{%- assign posts = site.posts -%}{%- else -%}{%- assign posts = site.posts | where_exp: "p", "p.categories contains cat" -%}{%- endif -%}
{%- assign by_year = posts | group_by_exp: "p", "p.date | date: '%Y'" -%}
{%- assign label = parts[0] | remove: " Blog" -%}{%- if parts[0] == "All" -%}{%- assign label = "All Posts" -%}{%- endif -%}
{%- if parts[0] == "Link Post" -%}{%- assign label = "Link Posts" -%}{%- elsif parts[0] == "YouTube Videos" -%}{%- assign label = "Videos" -%}{%- endif %}
<section id="{{ parts[0] | slugify }}" class="cat-panel mb-5" role="tabpanel" aria-labelledby="tab-{{ parts[0] | slugify }}">
  <h2 class="h4 fw-bold mb-3"><i class="fas {{ parts[1] }} me-2 cat-icon" aria-hidden="true"></i>{{ label }} <span class="small fw-normal text-body-secondary">{{ posts.size }} posts</span></h2>
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
            {%- if cat == "All" -%}{%- for c2 in cats offset: 1 -%}{%- assign cp = c2 | split: "|" -%}{%- if p.categories contains cp[0] %}<i class="fas {{ cp[1] }} cat-icon date-row-cat" title="{{ cp[0] }}" aria-hidden="true"></i>{% endif -%}{%- endfor -%}{%- endif %}
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
// Show one category at a time: the one in the address (#travel-blog), or All.
(function () {
  var cards = document.querySelectorAll(".cat-card");
  var panels = document.querySelectorAll(".cat-panel");
  function show(id, scroll) {
    if (!document.getElementById(id)) id = cards[0].dataset.cat;
    cards.forEach(function (c) {
      var on = c.dataset.cat === id;
      c.classList.toggle("is-active", on);
      c.setAttribute("aria-selected", on);
    });
    panels.forEach(function (p) { p.hidden = p.id !== id; });
    if (scroll) document.getElementById(id).scrollIntoView({ behavior: "smooth", block: "start" });
  }
  cards.forEach(function (c) {
    c.addEventListener("click", function (e) {
      e.preventDefault();
      history.replaceState(null, "", "#" + c.dataset.cat);
      show(c.dataset.cat, false);
    });
  });
  window.addEventListener("hashchange", function () { show(location.hash.slice(1), true); });
  show(location.hash.slice(1), location.hash.length > 1);
})();
</script>
