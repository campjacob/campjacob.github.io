---
title: Books
description: "The books I've read and listened to, with what I wrote or learned from them."
layout: foundation
nav_group: stream
author_sidebar: true
permalink: /books/
redirect_from:
  - /stream/books/
---
{%- comment -%}
  Everything I've read. Dated books are _stream/books/ files, so they're also in /stream/.
  Books without a real finish date can't be stream items (Jekyll would date them today), so
  they come from _data/books_undated.yml and sit under "Earlier". Books in progress are pages in
  _pages/books/ and join the stream only when finished. Filtering, sorting, and the
  list view are in the script below; without JS the covers still show, grouped by year.
{%- endcomment -%}
{%- assign books = site.stream | where: "source", "books" | sort: "date" | reverse -%}
{%- assign undated = site.data.books_undated -%}
{%- assign total = books.size | plus: undated.size -%}
{%- assign by_year = books | group_by_exp: "b", "b.date | date: '%Y'" -%}

<div class="my-4" id="books">

<header class="mb-3">
  <h1 class="fw-bolder">Books</h1>
  <p class="lead mb-2">{{ total }} books I've read or listened to, newest first. Each one with a date also shows up in my <a href="/stream/">stream</a>.</p>
</header>

{%- assign reading = site.pages | where: "layout", "book_reading" | sort: "title" -%}
{%- if reading.size > 0 -%}
<section class="mb-4" id="books-reading">
  <h2 class="h5 fw-bold border-bottom pb-1 mb-3">Currently reading <span class="fw-normal text-body-secondary small">{{ reading | size }}</span></h2>
  <div class="book-grid">
    {%- for b in reading -%}
    {% include book-link-icons.htm book=b.book %}
    <div class="book-tile">
      <a href="{{ b.url | relative_url }}" class="book-tile-link text-decoration-none text-body">
      <span class="stream-book-cover"><i class="fas fa-book" aria-hidden="true"></i>{% if b.book.image %}<img src="{{ b.book.image }}" alt="" loading="lazy" decoding="async" onerror="this.remove()">{% endif %}</span>
      <span class="book-tile-title">{{ b.title }}</span>
      <span class="book-tile-author">{{ b.book.author }}{% if b.book.year %}<span class="book-tile-meta"> ({{ b.book.year }})</span>{% endif %}</span>
      <span class="book-tile-meta book-tile-detail">{{ b.book.format }}{% if b.book.format %} &middot; {% endif %}{% if b.book.format == "Audiobook" %}Listening now{% else %}Reading now{% endif %}</span>
      </a>
      {{ link_icons }}
      <div class="book-tile-links">{% include book-links.htm book=b.book %}</div>
    </div>
    {%- endfor -%}
  </div>
</section>
{%- endif -%}

<div class="mb-2 d-none" id="books-tools">
  <div class="d-flex flex-wrap align-items-center gap-2 mb-2">
    <div class="d-flex flex-wrap gap-1" role="group" aria-label="Filter by format" id="books-format">
      <button type="button" class="btn btn-sm btn-outline-primary active" data-format="all">All <span class="badge text-bg-secondary"></span></button>
      <button type="button" class="btn btn-sm btn-outline-primary" data-format="audio">Audio <span class="badge text-bg-secondary"></span></button>
      <button type="button" class="btn btn-sm btn-outline-primary" data-format="print">Print <span class="badge text-bg-secondary"></span></button>
      <button type="button" class="btn btn-sm btn-outline-primary" data-format="ebook">Ebook <span class="badge text-bg-secondary"></span></button>
    </div>
    <div class="btn-group btn-group-sm ms-auto" role="group" aria-label="View" id="books-view">
      <button type="button" class="btn btn-outline-primary active" data-view="covers"><i class="fas fa-table-cells me-1" aria-hidden="true"></i>Covers</button>
      <button type="button" class="btn btn-outline-primary" data-view="list"><i class="fas fa-list me-1" aria-hidden="true"></i>List</button>
    </div>
  </div>
  <div class="d-flex flex-wrap align-items-center gap-2">
    <select class="form-select form-select-sm w-auto" id="books-category" aria-label="Filter by category">
      <option value="all">All categories</option>
    </select>
    <select class="form-select form-select-sm w-auto" id="books-links" aria-label="Filter by type of link">
      <option value="all">All links</option>
      <option value="any">Has any link</option>
      <option value="review">I reviewed it</option>
      <option value="post">Blog posts</option>
      <option value="resource">Essays &amp; articles</option>
      <option value="mastodon">Mastodon posts</option>
      <option value="word">Dictionary words</option>
    </select>
    <select class="form-select form-select-sm w-auto" id="books-sort" aria-label="Sort books">
      <option value="newest">Newest read</option>
      <option value="oldest">Oldest read</option>
      <option value="title">Title</option>
      <option value="author">Author</option>
      <option value="year">Publication year</option>
    </select>
  </div>
</div>
<p class="small text-body-secondary mb-3 d-none" id="books-count" aria-live="polite"></p>

<div id="books-sections">
{%- for y in by_year -%}
<section class="mb-4 books-section">
  <h2 class="h5 fw-bold border-bottom pb-1 mb-3">{{ y.name }} <span class="fw-normal text-body-secondary small books-section-count">{{ y.items | size }}</span></h2>
  <div class="book-grid">
    {%- for b in y.items -%}
    {% include book-link-icons.htm book=b.book %}
    {%- if b.book.month_only -%}{%- assign read_text = b.date | date: "%b %Y" -%}{%- else -%}{%- assign read_text = b.date | date: "%b %-d, %Y" -%}{%- endif -%}
    <div class="book-tile" data-links="{{ link_keys | strip }}" data-format="{{ b.book.format_keys }}" data-category="{{ b.book.category | escape }}" data-title="{{ b.title | downcase | escape }}" data-author="{{ b.book.author_key | escape }}" data-year="{{ b.book.year }}" data-read="{{ b.date | date: '%Y-%m-%d' }}">
      <a href="{{ b.url | relative_url }}" class="book-tile-link text-decoration-none text-body">
      <span class="stream-book-cover"><i class="fas fa-book" aria-hidden="true"></i>{% if b.book.image %}<img src="{{ b.book.image }}" alt="" loading="lazy" decoding="async" onerror="this.remove()">{% endif %}</span>
      <span class="book-tile-title">{{ b.title }}</span>
      <span class="book-tile-author">{{ b.book.author }}{% if b.book.year %}<span class="book-tile-meta"> ({{ b.book.year }})</span>{% endif %}</span>
      <span class="book-tile-meta book-tile-detail">{{ b.book.format }}{% if b.book.format %} &middot; {% endif %}{{ read_text }}</span>
      </a>
      {{ link_icons }}
      <div class="book-tile-links">{% include book-links.htm book=b.book %}</div>
    </div>
    {%- endfor -%}
  </div>
</section>
{%- endfor -%}

{%- if undated.size > 0 -%}
<section class="mb-4 books-section">
  <h2 class="h5 fw-bold border-bottom pb-1 mb-3">Earlier <span class="fw-normal text-body-secondary small books-section-count">{{ undated | size }}</span></h2>
  <div class="book-grid">
    {%- for b in undated -%}
    {% include book-link-icons.htm book=b %}
    <div class="book-tile" data-links="{{ link_keys | strip }}" data-format="{{ b.format_keys }}" data-category="{{ b.category | escape }}" data-title="{{ b.title | downcase | escape }}" data-author="{{ b.author_key | escape }}" data-year="{{ b.year }}" data-read="">
      <a href="{{ b.link }}" class="book-tile-link text-decoration-none text-body" rel="noopener">
      <span class="stream-book-cover"><i class="fas fa-book" aria-hidden="true"></i>{% if b.image %}<img src="{{ b.image }}" alt="" loading="lazy" decoding="async" onerror="this.remove()">{% endif %}</span>
      <span class="book-tile-title">{{ b.title }}</span>
      <span class="book-tile-author">{{ b.author }}{% if b.year %}<span class="book-tile-meta"> ({{ b.year }})</span>{% endif %}</span>
      <span class="book-tile-meta book-tile-detail">{{ b.format }}{% if b.format %} &middot; {% endif %}Earlier</span>
      </a>
      {{ link_icons }}
      <div class="book-tile-links">{% include book-links.htm book=b %}</div>
    </div>
    {%- endfor -%}
  </div>
</section>
{%- endif -%}
</div>

<div class="book-grid d-none mb-4" id="books-flat"></div>
<p class="text-body-secondary d-none" id="books-empty">No books match those filters.</p>

</div>

<script>
// Format and category filters, sorting, and the covers/list toggle.
(function () {
  var root = document.getElementById("books");
  // Currently reading sits outside the filters, so it isn't in this list
  var tiles = Array.prototype.slice.call(document.querySelectorAll("#books-sections .book-tile"));
  tiles.forEach(function (t, i) { t.bookHome = t.parentNode; t.bookOrder = i; });
  var sections = document.getElementById("books-sections");
  var flat = document.getElementById("books-flat");
  var state = { format: "all", category: "all", links: "all", sort: "newest" };
  var linksSelect = document.getElementById("books-links");
  var categorySelect = document.getElementById("books-category");
  var sortSelect = document.getElementById("books-sort");
  var formatGroup = document.getElementById("books-format");
  var viewGroup = document.getElementById("books-view");

  function keys(t) { return (t.dataset.format || "").split(" "); }
  function linkKeys(t) { return (t.dataset.links || "").split(" ").filter(Boolean); }
  function article(s) { return s.replace(/^(the|a|an) /, ""); }
  function cmp(a, b) { return a < b ? -1 : a > b ? 1 : 0; }
  // Books without the value being sorted on always go last
  var sorters = {
    oldest: function (a, b) { return (!a.dataset.read - !b.dataset.read) || cmp(a.dataset.read, b.dataset.read); },
    title: function (a, b) { return cmp(article(a.dataset.title), article(b.dataset.title)); },
    author: function (a, b) { return (!a.dataset.author - !b.dataset.author) || cmp(a.dataset.author, b.dataset.author) || cmp(a.dataset.year, b.dataset.year); },
    year: function (a, b) { return (!a.dataset.year - !b.dataset.year) || (+b.dataset.year - +a.dataset.year); }
  };

  function render() {
    var shown = 0;
    tiles.forEach(function (t) {
      var ok = (state.format === "all" || keys(t).indexOf(state.format) > -1) &&
               (state.category === "all" || t.dataset.category === state.category) &&
               (state.links === "all" || (state.links === "any" ? linkKeys(t).length > 0 : linkKeys(t).indexOf(state.links) > -1));
      t.classList.toggle("d-none", !ok);
      if (ok) shown++;
    });
    if (state.sort === "newest") {
      tiles.forEach(function (t) { t.bookHome.appendChild(t); });
      root.querySelectorAll(".books-section").forEach(function (s) {
        var n = s.querySelectorAll(".book-tile:not(.d-none)").length;
        s.querySelector(".books-section-count").textContent = n;
        s.classList.toggle("d-none", n === 0);
      });
    } else {
      tiles.slice().sort(function (a, b) { return sorters[state.sort](a, b) || a.bookOrder - b.bookOrder; })
        .forEach(function (t) { flat.appendChild(t); });
    }
    sections.classList.toggle("d-none", state.sort !== "newest");
    flat.classList.toggle("d-none", state.sort === "newest" || shown === 0);
    document.getElementById("books-empty").classList.toggle("d-none", shown > 0);
    document.getElementById("books-count").textContent = "Showing " + shown + " of " + tiles.length;
  }

  // Counts on the format buttons
  formatGroup.querySelectorAll("[data-format]").forEach(function (b) {
    var f = b.dataset.format;
    var n = f === "all" ? tiles.length : tiles.filter(function (t) { return keys(t).indexOf(f) > -1; }).length;
    b.querySelector(".badge").textContent = n;
    if (n === 0) b.classList.add("d-none");
    b.addEventListener("click", function () {
      formatGroup.querySelector(".active").classList.remove("active");
      b.classList.add("active"); state.format = f; render();
    });
  });

  // Categories come from the books themselves
  var counts = {};
  tiles.forEach(function (t) { var c = t.dataset.category; if (c) counts[c] = (counts[c] || 0) + 1; });
  Object.keys(counts).sort().forEach(function (c) {
    var o = document.createElement("option"); o.value = c; o.textContent = c + " (" + counts[c] + ")"; categorySelect.appendChild(o);
  });
  categorySelect.addEventListener("change", function () { state.category = categorySelect.value; render(); });
  // Counts on the link types
  Array.prototype.forEach.call(linksSelect.options, function (o) {
    if (o.value === "all") return;
    var n = tiles.filter(function (t) { return o.value === "any" ? linkKeys(t).length > 0 : linkKeys(t).indexOf(o.value) > -1; }).length;
    o.textContent += " (" + n + ")";
    if (n === 0) o.hidden = true;
  });
  linksSelect.addEventListener("change", function () { state.links = linksSelect.value; render(); });
  sortSelect.addEventListener("change", function () { state.sort = sortSelect.value; render(); });

  function setView(v) {
    root.classList.toggle("books-list", v === "list");
    viewGroup.querySelectorAll("[data-view]").forEach(function (b) { b.classList.toggle("active", b.dataset.view === v); });
    try { localStorage.setItem("books-view", v); } catch (e) {}
  }
  viewGroup.querySelectorAll("[data-view]").forEach(function (b) {
    b.addEventListener("click", function () { setView(b.dataset.view); });
  });
  try { if (localStorage.getItem("books-view") === "list") setView("list"); } catch (e) {}

  document.getElementById("books-tools").classList.remove("d-none");
  document.getElementById("books-count").classList.remove("d-none");
  render();
})();
</script>
