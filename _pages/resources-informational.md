---
title: Resources
layout: foundation
nav_group: resources
author_sidebar: true
permalink: /resources/
---
{%- comment -%}
  Resources index in the Bootstrap "foundation" style. Type comes from the folder:
  _resources/essays/ (Essay), _resources/articles/ (Article), everything else in
  _resources/ (Informational). Essays are grouped by Ph.D. course (Course ID and
  Course Title in their front matter). Informational posts are grouped by tag.
{%- endcomment -%}
{%- assign all = site.resources | sort: "date" | reverse -%}
{%- assign essays = "" | split: "" -%}
{%- assign articles = "" | split: "" -%}
{%- assign informationals = "" | split: "" -%}
{%- for r in all -%}
  {%- if r.path contains "/essays/" -%}{%- assign essays = essays | push: r -%}
  {%- elsif r.path contains "/articles/" -%}{%- assign articles = articles | push: r -%}
  {%- else -%}{%- assign informationals = informationals | push: r -%}{%- endif -%}
{%- endfor -%}
{%- assign oldest = all | last -%}
{%- assign newest = all | first -%}

{%- comment -%} Essays by course; essays without course details go last as "Other Essays". {%- endcomment -%}
{%- assign course_keys = "" | split: "" -%}
{%- for e in essays -%}
  {%- assign cid = e["Course ID"] | strip -%}
  {%- assign ctitle = e["Course Title"] | strip -%}
  {%- if cid != "" -%}{%- assign key = cid | append: ": " | append: ctitle -%}{%- assign course_keys = course_keys | push: key -%}{%- endif -%}
{%- endfor -%}
{%- assign course_keys = course_keys | uniq | sort -%}

{%- comment -%} Informational groups by tag; anything untagged falls into Other. {%- endcomment -%}
{%- assign rm_overview_url = "/resources/research-methods-evidence-based-practice" -%}
{%- assign research = "" | split: "" -%}
{%- for r in informationals -%}
  {%- if r.tags contains "Research Methods" -%}{%- unless r.tags contains "Directions Program Evaluation" or r.url == rm_overview_url -%}{%- assign research = research | push: r -%}{%- endunless -%}{%- endif -%}
{%- endfor -%}
{%- assign directions = informationals | where: "tags", "Directions Program Evaluation" -%}
{%- assign directions_articles = articles | where: "tags", "Directions Program Evaluation" -%}
{%- assign talks = "" | split: "" -%}
{%- assign other = "" | split: "" -%}
{%- for r in informationals -%}
  {%- if r.tags contains "Research Methods" or r.tags contains "Directions Program Evaluation" or r.url == rm_overview_url -%}
  {%- elsif r.tags contains "Presentation" or r.tags contains "Handout" -%}{%- assign talks = talks | push: r -%}
  {%- else -%}{%- assign other = other | push: r -%}{%- endif -%}
{%- endfor -%}

<article class="resources-index">

<header class="my-4">
  <h1 class="fw-bolder">Resources</h1>
  <p class="lead mb-1">I've compiled academic writing and notes over the years. Some come from my Bachelor's (BASW) and Master's (MSW) in Social Work at Eastern Washington University (2007–2009), and many essays come from my Ph.D. in Transformative Studies at the California Institute of Integral Studies, which I started in 2019. For non-academic writing, see my <a href="/blog/">blog</a>. Talks and presentations from teaching and events are in my <a href="https://presentations.jacobrcampbell.com">presentations</a> section.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-book-open" aria-hidden="true"></i> {{ all | size }} resources: {{ essays | size }} essays, {{ articles | size }} articles, and {{ informationals | size }} informational posts, {{ oldest.date | date: "%Y" }}–{{ newest.date | date: "%Y" }}.</p>
</header>

<!-- Section Cards -->
<section class="my-4">
  <div class="row row-cols-1 row-cols-md-3 g-3">
    <div class="col">
      <a href="#essays" class="card h-100 shadow-sm text-decoration-none">
        <div class="card-body">
          <h2 class="h5 fw-bold text-body"><i class="fas fa-feather-alt me-2 orange" aria-hidden="true"></i>Academic Essays</h2>
          <p class="card-text small text-body-secondary mb-0">Writing from my Ph.D. coursework, grouped by course.</p>
        </div>
        <div class="card-footer bg-transparent small text-body-secondary">{{ essays | size }} essays</div>
      </a>
    </div>
    <div class="col">
      <a href="#articles" class="card h-100 shadow-sm text-decoration-none">
        <div class="card-body">
          <h2 class="h5 fw-bold text-body"><i class="fas fa-file-alt me-2 orange" aria-hidden="true"></i>Articles</h2>
          <p class="card-text small text-body-secondary mb-0">Longer papers and reports, mostly on social work practice and research.</p>
        </div>
        <div class="card-footer bg-transparent small text-body-secondary">{{ articles | size }} articles</div>
      </a>
    </div>
    <div class="col">
      <a href="#informational" class="card h-100 shadow-sm text-decoration-none">
        <div class="card-body">
          <h2 class="h5 fw-bold text-body"><i class="fas fa-lightbulb me-2 orange" aria-hidden="true"></i>Informational</h2>
          <p class="card-text small text-body-secondary mb-0">Research methods notes, a program evaluation, presentations, and handouts.</p>
        </div>
        <div class="card-footer bg-transparent small text-body-secondary">{{ informationals | size }} posts</div>
      </a>
    </div>
  </div>
</section>
<!-- End Section Cards -->

<!-- Academic Essays -->
<section class="my-5" id="essays">
  <div class="d-flex flex-wrap justify-content-between align-items-baseline gap-2 mb-1">
    <h2 class="h4 fw-bold mb-0">Academic Essays</h2>
    <a href="/resources/essays/" class="small text-decoration-none">All essays by date &rarr;</a>
  </div>
  <p class="text-body-secondary small">Essays from the Ph.D. in Transformative Studies, grouped by course.</p>

  <div class="accordion" id="essaysByCourse">
    {%- for key in course_keys -%}
    {%- assign anchor = key | slugify -%}
    {%- assign cid = key | split: ": " | first -%}
    {%- assign in_course = "" | split: "" -%}
    {%- for e in essays -%}{%- assign ecid = e["Course ID"] | strip -%}{%- if ecid == cid -%}{%- assign in_course = in_course | push: e -%}{%- endif -%}{%- endfor -%}
    {%- assign in_course = in_course | sort: "date" -%}
    {%- assign first_e = in_course | first -%}
    <div class="accordion-item" id="{{ anchor }}">
      <h3 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{{ anchor }}" aria-expanded="false" aria-controls="collapse-{{ anchor }}">
          <span class="fw-semibold flex-grow-1 text-start">{{ key }}</span>
          <span class="small text-body-secondary ms-3 me-3 d-none d-sm-inline">{{ first_e.date | date: "%Y" }}</span>
          <span class="badge rounded-pill text-bg-secondary me-2">{{ in_course | size }}</span>
        </button>
      </h3>
      <div id="collapse-{{ anchor }}" class="accordion-collapse collapse" data-bs-parent="#essaysByCourse">
        <ul class="list-group list-group-flush">
          {%- for e in in_course -%}
          <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
            <a href="{{ e.url | relative_url }}" class="text-decoration-none">{{ e.title | escape }}</a>
            <small class="text-body-secondary text-nowrap">{{ e.date | date: "%b %-d, %Y" }}</small>
          </li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
    {%- endfor -%}

    {%- assign no_course = "" | split: "" -%}
    {%- for e in essays -%}{%- assign ecid = e["Course ID"] | strip -%}{%- if ecid == "" -%}{%- assign no_course = no_course | push: e -%}{%- endif -%}{%- endfor -%}
    {%- if no_course.size > 0 -%}
    <div class="accordion-item" id="other-essays">
      <h3 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-other-essays" aria-expanded="false" aria-controls="collapse-other-essays">
          <span class="fw-semibold flex-grow-1 text-start">Other Essays</span>
          <span class="badge rounded-pill text-bg-secondary me-2">{{ no_course | size }}</span>
        </button>
      </h3>
      <div id="collapse-other-essays" class="accordion-collapse collapse" data-bs-parent="#essaysByCourse">
        <ul class="list-group list-group-flush">
          {%- for e in no_course -%}
          <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
            <a href="{{ e.url | relative_url }}" class="text-decoration-none">{{ e.title | escape }}</a>
            <small class="text-body-secondary text-nowrap">{{ e.date | date: "%b %-d, %Y" }}</small>
          </li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
    {%- endif -%}
  </div>
</section>
<!-- End Academic Essays -->

<!-- Articles -->
<section class="my-5" id="articles">
  <div class="d-flex flex-wrap justify-content-between align-items-baseline gap-2 mb-1">
    <h2 class="h4 fw-bold mb-0">Articles</h2>
    <a href="/resources/articles/" class="small text-decoration-none">All articles &rarr;</a>
  </div>
  <p class="text-body-secondary small">Academically focused papers and reports, newest first.</p>
  <div class="card shadow-sm">
    <ul class="list-group list-group-flush">
      {%- for r in articles limit: 6 -%}
      {% include resource-list-item.htm resource=r %}
      {%- endfor -%}
    </ul>
    <div class="card-footer bg-transparent text-end small">
      <a href="/resources/articles/" class="text-decoration-none">Show all {{ articles | size }} articles &rarr;</a>
    </div>
  </div>
</section>
<!-- End Articles -->

<!-- Informational -->
<section class="my-5" id="informational">
  <h2 class="h4 fw-bold mb-1">Informational</h2>
  <p class="text-body-secondary small">Posts from notes I took during my studies, and presentations I have given.</p>

  <div class="row row-cols-1 row-cols-lg-2 g-3">
    <div class="col" id="research-methods">
      <div class="card h-100 shadow-sm">
        <div class="card-header fw-bold">Research Methods</div>
        <div class="card-body small pb-0">
          <p>Research methods can be intimidating. Start with the overview, then go topic by topic.</p>
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item"><a href="{{ rm_overview_url | relative_url }}" class="text-decoration-none fw-semibold">Research Methods &amp; Evidence-Based Practice</a> <span class="badge text-bg-light border ms-1">Overview</span></li>
          {%- assign research_sorted = research | sort: "title" -%}
          {%- for r in research_sorted -%}
          <li class="list-group-item"><a href="{{ r.url | relative_url }}" class="text-decoration-none">{{ r.title | escape }}</a></li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
    <div class="col" id="directions-program-evaluation">
      <div class="card h-100 shadow-sm">
        <div class="card-header fw-bold">Directions Program Evaluation</div>
        <div class="card-body small pb-0">
          <p>My Master's terminal project was an in-depth program evaluation. Start with the <a href="/resources/overview-of-the-crisis-residential-centers-directions-program-evaluation">overview of the Directions Program Evaluation</a>.</p>
        </div>
        <ul class="list-group list-group-flush">
          {%- for r in directions -%}
          <li class="list-group-item"><a href="{{ r.url | relative_url }}" class="text-decoration-none">{{ r.title | escape }}</a></li>
          {%- endfor -%}
          {%- for r in directions_articles -%}
          <li class="list-group-item"><a href="{{ r.url | relative_url }}" class="text-decoration-none">{{ r.title | escape }}</a> <span class="badge text-bg-light border ms-1">Article</span></li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
    <div class="col" id="presentations-and-handouts">
      <div class="card h-100 shadow-sm">
        <div class="card-header fw-bold">Presentations and Handouts</div>
        <div class="card-body small pb-0">
          <p>Earlier presentations and their handouts. Newer talks are on my <a href="https://presentations.jacobrcampbell.com">presentations</a> site.</p>
        </div>
        <ul class="list-group list-group-flush">
          {%- assign talks_sorted = talks | sort: "title" -%}
          {%- for r in talks_sorted -%}
          <li class="list-group-item"><a href="{{ r.url | relative_url }}" class="text-decoration-none">{{ r.title | escape }}</a>{% if r.tags contains "Handout" %} <span class="badge text-bg-light border ms-1">Handout</span>{% endif %}</li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
    <div class="col" id="other-informational">
      <div class="card h-100 shadow-sm">
        <div class="card-header fw-bold">Other</div>
        <div class="card-body small pb-0">
          <p>Writing feedback lists and other posts that don't fit elsewhere.</p>
        </div>
        <ul class="list-group list-group-flush">
          {%- assign other_sorted = other | sort: "title" -%}
          {%- for r in other_sorted -%}
          <li class="list-group-item"><a href="{{ r.url | relative_url }}" class="text-decoration-none">{{ r.title | escape }}</a></li>
          {%- endfor -%}
        </ul>
      </div>
    </div>
  </div>
</section>
<!-- End Informational -->

</article>

<script>
// Open the accordion item named in the URL (e.g. /resources/#tsd-8130-transdisciplinarity)
document.addEventListener("DOMContentLoaded", function () {
  var id = decodeURIComponent(location.hash.slice(1));
  var target = id && document.getElementById("collapse-" + id);
  if (target && window.bootstrap) new bootstrap.Collapse(target, { toggle: true });
});
</script>
