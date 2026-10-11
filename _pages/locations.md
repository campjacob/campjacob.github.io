---
title: Locations
layout: foundation
nav_group: blog
permalink: /locations/
---
{%- comment -%} Places come from the "L-- " tags on posts; coordinates and country from _data/locations.yml. A tag missing from the data file is still listed, under "Not on the map yet". {%- endcomment -%}
{%- assign countries = "" | split: "" -%}
{%- for loc in site.data.locations -%}
  {%- assign countries = countries | push: loc[1].country -%}
{%- endfor -%}
{%- assign countries = countries | uniq | sort -%}
{%- assign others = countries | where_exp: "c", "c != 'United States'" -%}
{%- assign countries = "United States" | split: "|" | concat: others -%}
{%- assign unmapped = "" | split: "" -%}
{%- for tag in site.tags -%}
  {%- if tag[0] contains "L-- " -%}
    {%- assign key = tag[0] | remove_first: "L-- " -%}
    {%- unless site.data.locations[key] -%}{%- assign unmapped = unmapped | push: key -%}{%- endunless -%}
  {%- endif -%}
{%- endfor -%}
{%- assign located_count = 0 -%}
{%- for p in site.posts -%}{%- for t in p.tags -%}{%- if t contains "L-- " -%}{%- assign located_count = located_count | plus: 1 -%}{%- break -%}{%- endif -%}{%- endfor -%}{%- endfor -%}

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css">

<article class="locations-index">

<header class="my-4">
  {% include blog-views.htm %}
  <h1 class="fw-bolder">Locations</h1>
  <p class="lead mb-1">Where my posts were written, or what they are about: home in the Tri-Cities and Spokane, plus trips through Europe, South America, the Caribbean, and Mexico.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-map-marked-alt" aria-hidden="true"></i> {{ located_count }} posts from {{ site.data.locations | size | plus: unmapped.size }} places in {{ countries | size }} countries.</p>
</header>

<section class="mb-5" aria-label="Map of post locations">
  <div id="locations-map" class="rounded-top shadow-sm border" style="height: min(60vh, 480px);"></div>

  <div id="loc-panel" class="card rounded-top-0 border-top-0 shadow-sm" tabindex="0" aria-live="polite" hidden>
    <div class="card-header d-flex align-items-center gap-2">
      <button type="button" class="btn btn-outline-secondary btn-sm" data-step="-1" aria-label="Previous place"><i class="fas fa-chevron-left" aria-hidden="true"></i></button>
      <div class="flex-grow-1 text-center">
        <div class="fw-bold" id="loc-name"></div>
        <div class="small text-body-secondary" id="loc-meta"></div>
      </div>
      <button type="button" class="btn btn-outline-secondary btn-sm" data-step="1" aria-label="Next place"><i class="fas fa-chevron-right" aria-hidden="true"></i></button>
    </div>
    <div class="card-body">
      <ul class="list-unstyled mb-0 row row-cols-1 row-cols-md-2 g-1" id="loc-posts"></ul>
      <button type="button" class="btn btn-link btn-sm px-0 mt-1" id="loc-more" hidden></button>
    </div>
  </div>
  <p class="text-body-secondary small mt-2 mb-0">Select a place on the map, or step through them with the arrows (or the left and right arrow keys). Numbers are post counts; zoom in to split up the grouped places.</p>
</section>

<section class="mb-5">
  <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 gap-2">
    <h2 class="h4 fw-bold mb-0">By Country</h2>
    <div class="btn-group btn-group-sm" role="group" aria-label="Expand or collapse countries">
      <button type="button" class="btn btn-outline-secondary" data-locations-toggle="show">Expand all</button>
      <button type="button" class="btn btn-outline-secondary" data-locations-toggle="hide">Collapse all</button>
    </div>
  </div>

  <div class="accordion" id="locationsAccordion">
  {%- for country in countries -%}
    {%- assign c_anchor = country | slugify -%}
    {%- assign c_places = 0 -%}{%- assign c_posts = 0 -%}
    {%- for loc in site.data.locations -%}{%- if loc[1].country == country -%}
      {%- assign tag = "L-- " | append: loc[0] -%}
      {%- assign c_places = c_places | plus: 1 -%}{%- assign c_posts = c_posts | plus: site.tags[tag].size -%}
    {%- endif -%}{%- endfor %}
    <div class="accordion-item">
      <h3 class="accordion-header" id="h-{{ c_anchor }}">
        <button class="accordion-button{% unless forloop.first %} collapsed{% endunless %}" type="button" data-bs-toggle="collapse" data-bs-target="#c-{{ c_anchor }}" aria-expanded="{% if forloop.first %}true{% else %}false{% endif %}" aria-controls="c-{{ c_anchor }}">
          <span class="d-flex flex-grow-1 align-items-baseline me-3">
            <span class="fw-bold">{{ country }}</span>
            <span class="ms-auto small text-body-secondary">{{ c_places }} {% if c_places == 1 %}place{% else %}places{% endif %} &middot; {{ c_posts }} {% if c_posts == 1 %}post{% else %}posts{% endif %}</span>
          </span>
        </button>
      </h3>
      <div id="c-{{ c_anchor }}" class="accordion-collapse collapse{% if forloop.first %} show{% endif %}" aria-labelledby="h-{{ c_anchor }}">
        <div class="accordion-body">
          <div class="row row-cols-1 row-cols-md-2 g-3">
          {%- for loc in site.data.locations -%}{%- if loc[1].country == country -%}
            {%- assign tag = "L-- " | append: loc[0] -%}
            {%- assign posts = site.tags[tag] -%}
            <div class="col">
              <section id="l-{{ loc[0] | slugify }}" class="h-100" data-country="c-{{ c_anchor }}">
                <h4 class="h6 fw-bold d-flex align-items-baseline mb-2">
                  <a href="#locations-map" class="text-reset text-decoration-none" data-show-place="l-{{ loc[0] | slugify }}" title="Show on the map"><i class="fas fa-map-pin me-2" style="color: var(--bs-primary);" aria-hidden="true"></i>{{ loc[1].place }}{% if loc[1].region %}<span class="fw-normal text-body-secondary">, {{ loc[1].region }}</span>{% endif %}</a>
                  <span class="badge rounded-pill text-bg-secondary ms-2">{{ posts.size }}</span>
                </h4>
                <ul class="list-unstyled small mb-0">
                  {%- for post in posts -%}
                  <li{% if forloop.index > 5 %} class="d-none extra"{% endif %}><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a> <span class="text-body-secondary text-nowrap">{{ post.date | date: "%b %Y" }}</span></li>
                  {%- endfor -%}
                </ul>
                {%- if posts.size > 5 %}
                <button type="button" class="btn btn-link btn-sm px-0 location-more">Show all {{ posts.size }} posts</button>
                {%- endif %}
              </section>
            </div>
          {%- endif -%}{%- endfor %}
          </div>
        </div>
      </div>
    </div>
  {%- endfor %}
  </div>

  {%- if unmapped.size > 0 %}
  <div class="mt-4">
    <h3 class="h6 fw-bold">Not on the map yet</h3>
    <ul class="small">
    {%- for key in unmapped -%}
      {%- assign tag = "L-- " | append: key %}
      <li id="l-{{ key | slugify }}"><strong>{{ key }}</strong>: {% for post in site.tags[tag] %}<a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}</li>
    {%- endfor %}
    </ul>
  </div>
  {%- endif %}
</section>

</article>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>
<script>
(function () {
  // Same order as the list below: United States first, then countries A to Z.
  var places = [
  {%- for country in countries -%}{%- for loc in site.data.locations -%}{%- if loc[1].country == country -%}
    {%- assign tag = "L-- " | append: loc[0] -%}
    {%- assign posts = site.tags[tag] %}
    { name: {{ loc[1].place | jsonify }}, region: {{ loc[1].region | jsonify }}, country: {{ loc[1].country | jsonify }}, lat: {{ loc[1].lat }}, lng: {{ loc[1].lng }}, anchor: "l-{{ loc[0] | slugify }}",
      posts: [{% for post in posts %}[{{ post.title | jsonify }}, {{ post.url | relative_url | jsonify }}, {{ post.date | date: "%b %Y" | jsonify }}]{% unless forloop.last %},{% endunless %}{% endfor %}] },
  {%- endif -%}{%- endfor -%}{%- endfor %}
  ];
  places.forEach(function (p) { p.where = p.region ? p.region + ", " + p.country : p.country; });

  var map = L.map("locations-map", { scrollWheelZoom: false, worldCopyJump: true });
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  // OpenStreetMap has no dark tiles, so dark mode inverts the light ones.
  function applyTheme() {
    var dark = document.documentElement.getAttribute("data-bs-theme") === "dark";
    map.getPane("tilePane").style.filter = dark ? "invert(1) hue-rotate(180deg) brightness(0.9) contrast(0.9)" : "";
  }
  applyTheme();
  new MutationObserver(applyTheme).observe(document.documentElement, { attributes: true, attributeFilter: ["data-bs-theme"] });

  function size(n) { return Math.round(22 + Math.sqrt(n) * 4); }
  function pinIcon(p, selected) {
    var s = size(p.posts.length);
    return L.divIcon({ className: "", iconSize: [s, s], html: '<span class="loc-pin' + (selected ? ' is-selected' : '') + '" style="width:' + s + 'px;height:' + s + 'px">' + p.posts.length + '</span>' });
  }

  // Nearby places merge into one circle showing their total posts; zooming in splits them.
  var cluster = L.markerClusterGroup({
    maxClusterRadius: 40, showCoverageOnHover: false, spiderfyOnMaxZoom: true,
    iconCreateFunction: function (c) {
      var total = c.getAllChildMarkers().reduce(function (sum, m) { return sum + m.place.posts.length; }, 0);
      var s = size(total) + 6;
      return L.divIcon({ className: "", iconSize: [s, s], html: '<span class="loc-pin loc-cluster" style="width:' + s + 'px;height:' + s + 'px">' + total + '</span>' });
    }
  });
  var markers = places.map(function (p, i) {
    var m = L.marker([p.lat, p.lng], { icon: pinIcon(p, false), title: p.name + ", " + p.where, riseOnHover: true });
    m.place = p;
    m.on("click", function () { select(i, false); });
    cluster.addLayer(m);
    return m;
  });
  map.addLayer(cluster);
  map.fitBounds(cluster.getBounds(), { padding: [20, 20] });

  var panel = document.getElementById("loc-panel");
  var list = document.getElementById("loc-posts");
  var more = document.getElementById("loc-more");
  var current = -1;
  function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

  function render(showAll) {
    var p = places[current], n = p.posts.length, shown = showAll ? n : Math.min(n, 6);
    document.getElementById("loc-name").textContent = p.name;
    document.getElementById("loc-meta").textContent = p.where + " · " + n + (n === 1 ? " post" : " posts") + " · " + (current + 1) + " of " + places.length;
    list.innerHTML = p.posts.slice(0, shown).map(function (x) {
      return '<li class="col small"><a href="' + x[1] + '">' + esc(x[0]) + '</a> <span class="text-body-secondary text-nowrap">' + x[2] + '</span></li>';
    }).join("");
    more.hidden = shown === n;
    more.textContent = "Show all " + n + " posts";
  }

  // zoom: move the map to the place (stepping with the arrows); a click on the map leaves the view alone.
  function select(i, zoom) {
    if (current >= 0) markers[current].setIcon(pinIcon(places[current], false));
    current = (i + places.length) % places.length;
    var m = markers[current];
    m.setIcon(pinIcon(places[current], true));
    m.setZIndexOffset(1000);
    if (zoom) cluster.zoomToShowLayer(m, function () { map.panTo(m.getLatLng()); });
    panel.hidden = false;
    render(false);
  }

  more.addEventListener("click", function () { render(true); });
  panel.addEventListener("click", function (e) {
    var b = e.target.closest("[data-step]");
    if (b) select(current + Number(b.dataset.step), true);
  });
  [panel, document.getElementById("locations-map")].forEach(function (el) {
    el.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft" || e.key === "ArrowRight") { e.preventDefault(); select(current + (e.key === "ArrowRight" ? 1 : -1), true); }
    });
  });

  // Start on the place with the most posts, without zooming away from the world view.
  var most = 0;
  places.forEach(function (p, i) { if (p.posts.length > places[most].posts.length) most = i; });
  select(most, false);

  document.addEventListener("click", function (e) {
    var show = e.target.closest("[data-show-place]");
    if (show) {
      e.preventDefault();
      var i = places.findIndex(function (p) { return p.anchor === show.dataset.showPlace; });
      document.getElementById("locations-map").scrollIntoView({ behavior: "smooth", block: "center" });
      if (i >= 0) select(i, true);
      return;
    }
    var moreList = e.target.closest(".location-more");
    if (moreList) { moreList.parentNode.querySelectorAll(".extra").forEach(function (li) { li.classList.remove("d-none"); }); moreList.remove(); return; }
    var t = e.target.closest("[data-locations-toggle]");
    if (t) document.querySelectorAll("#locationsAccordion .accordion-collapse").forEach(function (p) { bootstrap.Collapse.getOrCreateInstance(p, { toggle: false })[t.dataset.locationsToggle](); });
  });

  // Old links such as /locations/#l-spokane-washington select that place.
  if (location.hash.indexOf("#l-") === 0) {
    var h = places.findIndex(function (p) { return "#" + p.anchor === location.hash; });
    if (h >= 0) select(h, true);
  }
})();
</script>
