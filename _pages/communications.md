---
title: Communications Archive
layout: foundation
nav_group: communications
author_sidebar: true
permalink: /communications/
---
{%- assign all = site.communications | sort: "date" | reverse -%}
{%- comment -%} Newsletters are any group with "Newsletter" in its name; they have no semesters. {%- endcomment -%}
{%- assign newsletters = all | where_exp: "c", "c.group contains 'Newsletter'" -%}
{%- assign classes = "" | split: "" -%}
{%- for c in all -%}{%- if c.semester -%}{%- unless c.group contains "Newsletter" -%}{%- assign classes = classes | push: c -%}{%- endunless -%}{%- endif -%}{%- endfor -%}
{%- assign latest = classes | first -%}
{%- assign current_sem = latest.semester -%}
{%- assign current = classes | where: "semester", current_sem -%}
{%- assign current_groups = current | group_by: "group" | sort: "name" -%}
{%- assign by_group = classes | group_by: "group" | sort: "name" -%}
{%- assign first_email = all | last -%}
{%- assign card_limit = 5 -%}

<article class="communications-index">

<header class="my-4">
  <h1 class="fw-bolder">Communications Archive</h1>
  <p class="lead mb-1">In addition to posting assignment information in my university's learning management system, I email students the information they need for the week. I use <a href="https://emailoctopus.com/?urli=6v4df">EmailOctopus</a><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> to send these and let students choose which email address they want. I archive all of these communications, along with my newsletter, here.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-envelope" aria-hidden="true"></i> {{ all | size }} emails across {{ by_group | size }} courses{% if newsletters.size > 0 %} and the newsletter{% endif %}, {{ first_email.date | date: "%Y" }}–{{ latest.date | date: "%Y" }}.</p>
</header>

<!-- Current Semester -->
<section class="my-4">
  <h2 class="h4 fw-bold mb-3"><span class="badge me-2" style="background-color: var(--bs-primary);">Current</span>{{ current_sem }}</h2>
  <div class="row row-cols-1 row-cols-md-2 g-3">
    {%- for group in current_groups -%}
    {%- assign anchor = group.name | slugify -%}
    <div class="col">
      <div class="card h-100 shadow-sm">
        <div class="card-header d-flex justify-content-between align-items-center">
          <a class="fw-bold text-decoration-none text-body" href="#{{ anchor }}" data-open-group="{{ anchor }}">{{ group.name }}</a>
          <span class="badge rounded-pill text-bg-secondary">{{ group.items | size }}</span>
        </div>
        <ul class="list-group list-group-flush">
          {%- for item in group.items limit: card_limit -%}
          <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
            <a href="{{ item.url | relative_url }}" class="text-decoration-none">{{ item.title | remove: current_sem | strip }}</a>
            <small class="text-body-secondary text-nowrap">{{ item.date | date: "%b %-d" }}</small>
          </li>
          {%- endfor -%}
        </ul>
        {%- assign group_count = group.items | size -%}
        {%- if group_count > card_limit -%}
        <div class="card-footer bg-transparent text-end small">
          <a href="#{{ anchor }}" class="text-decoration-none">Show all {{ group_count }} &rarr;</a>
        </div>
        {%- endif -%}
      </div>
    </div>
    {%- endfor -%}
  </div>
</section>
<!-- End Current Semester -->

{%- if newsletters.size > 0 -%}
<!-- Newsletter -->
<section class="my-5" id="newsletter">
  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-1">
    <h2 class="h4 fw-bold mb-0"><i class="fas fa-newspaper me-2" aria-hidden="true"></i>Newsletter</h2>
    <a href="/email-signup/" class="btn btn-sm btn-primary"><i class="fas fa-envelope-open-text me-1" aria-hidden="true"></i> Sign up for the newsletter</a>
  </div>
  <p class="text-body-secondary small">My occasional newsletter, separate from class emails. Newest issues first.</p>
  <div class="card shadow-sm">
    <ul class="list-group list-group-flush">
      {%- for item in newsletters limit: 3 -%}
      <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
        <a href="{{ item.url | relative_url }}" class="text-decoration-none">{{ item.title }}</a>
        <small class="text-body-secondary text-nowrap">{{ item.date | date: "%b %-d, %Y" }}</small>
      </li>
      {%- endfor -%}
    </ul>
    {%- if newsletters.size > 3 -%}
    <div class="collapse" id="allNewsletterIssues">
      <ul class="list-group list-group-flush border-top">
        {%- for item in newsletters offset: 3 -%}
        <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
          <a href="{{ item.url | relative_url }}" class="text-decoration-none">{{ item.title }}</a>
          <small class="text-body-secondary text-nowrap">{{ item.date | date: "%b %-d, %Y" }}</small>
        </li>
        {%- endfor -%}
      </ul>
    </div>
    <div class="card-footer bg-transparent text-end small">
      <a class="text-decoration-none" data-bs-toggle="collapse" href="#allNewsletterIssues" role="button" aria-expanded="false" aria-controls="allNewsletterIssues">Show all {{ newsletters | size }} issues &rarr;</a>
    </div>
    {%- endif -%}
  </div>
</section>
<!-- End Newsletter -->
{%- endif -%}

<!-- Archive by Course -->
<section class="my-5">
  <h2 class="h4 fw-bold mb-1">All Courses</h2>
  <p class="text-body-secondary small">Emails grouped by course, then by semester, newest first.</p>

  <div class="accordion" id="communicationsArchive">
    {%- for group in by_group -%}
    {%- assign anchor = group.name | slugify -%}
    {%- assign newest = group.items | first -%}
    {%- assign oldest = group.items | last -%}
    {%- assign semesters = group.items | group_by: "semester" -%}
    {%- assign y_old = oldest.date | date: "%Y" -%}
    {%- assign y_new = newest.date | date: "%Y" -%}
    <div class="accordion-item" id="{{ anchor }}">
      <h3 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{{ anchor }}" aria-expanded="false" aria-controls="collapse-{{ anchor }}">
          <span class="fw-semibold me-auto">{{ group.name }}</span>
          <span class="small text-body-secondary me-3 d-none d-sm-inline">{{ y_old }}{% if y_old != y_new %}–{{ y_new }}{% endif %} &middot; {{ semesters | size }} semester{% if semesters.size != 1 %}s{% endif %}</span>
          <span class="badge rounded-pill text-bg-secondary me-2">{{ group.items | size }}</span>
        </button>
      </h3>
      <div id="collapse-{{ anchor }}" class="accordion-collapse collapse" data-bs-parent="#communicationsArchive">
        <div class="accordion-body">
          {%- for sem in semesters -%}
          <h4 class="h6 fw-bold mt-{% if forloop.first %}0{% else %}3{% endif %} mb-2">{{ sem.name | default: "Other" }} <span class="fw-normal text-body-secondary small">({{ sem.items | size }})</span></h4>
          <ul class="list-unstyled mb-0 ms-1">
            {%- for item in sem.items -%}
            <li class="d-flex justify-content-between align-items-baseline gap-2 py-1 border-bottom border-light-subtle">
              <a href="{{ item.url | relative_url }}" class="text-decoration-none">{{ item.title }}</a>
              <small class="text-body-secondary text-nowrap">{{ item.date | date: "%b %-d, %Y" }}</small>
            </li>
            {%- endfor -%}
          </ul>
          {%- endfor -%}
        </div>
      </div>
    </div>
    {%- endfor -%}
  </div>
</section>
<!-- End Archive by Course -->

<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
  <hr />
  <ol>
    <li id="fn1"><p>Link an affiliate link<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
  </ol>
</section>

</article>

<script>
// Open the course matching the URL hash (e.g. /communications/#sowk-486) or a clicked current-semester card
(function () {
  function openGroup(id, scroll) {
    var item = document.getElementById(id);
    var panel = document.getElementById("collapse-" + id);
    if (!item || !panel || !window.bootstrap) return;
    bootstrap.Collapse.getOrCreateInstance(panel, { toggle: false }).show();
    if (scroll) setTimeout(function () { item.scrollIntoView({ behavior: "smooth", block: "start" }); }, 250);
  }
  window.addEventListener("load", function () {
    if (location.hash) openGroup(location.hash.slice(1), true);
  });
  window.addEventListener("hashchange", function () { openGroup(location.hash.slice(1), true); });
})();
</script>
