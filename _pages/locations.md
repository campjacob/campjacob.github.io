---
title: Locations
layout: foundation
nav_group: blog
permalink: /locations/
---
{%- comment -%} Places come from the posts' `locations:` field; coordinates and country from _data/locations.yml. A place missing from the data file is still listed, under "Not on the map yet". {%- endcomment -%}
{%- assign countries = "" | split: "" -%}
{%- for loc in site.data.locations -%}
  {%- assign countries = countries | push: loc[1].country -%}
{%- endfor -%}
{%- assign countries = countries | uniq | sort -%}
{%- assign others = countries | where_exp: "c", "c != 'United States'" -%}
{%- assign countries = "United States" | split: "|" | concat: others -%}
{%- assign unmapped = "" | split: "" -%}
{%- for p in site.posts -%}{%- for key in p.locations -%}
  {%- unless site.data.locations[key] -%}{%- assign unmapped = unmapped | push: key -%}{%- endunless -%}
{%- endfor -%}{%- endfor -%}
{%- assign unmapped = unmapped | uniq | sort -%}
{%- assign located_count = 0 -%}
{%- assign located = site.posts | where_exp: "p", "p.locations.size > 0" -%}{%- assign located_count = located.size -%}

<article class="locations-index">

<header class="my-4">
  {% include blog-views.htm %}
  <h1 class="fw-bolder">Locations</h1>
  <p class="lead mb-1">Where my posts were written, or what they are about: home in the Tri-Cities and Spokane, plus trips through Europe, South America, the Caribbean, and Mexico.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-map-marked-alt" aria-hidden="true"></i> {{ located_count }} posts from {{ site.data.locations | size | plus: unmapped.size }} places in {{ countries | size }} countries.</p>
</header>

<section class="mb-5" aria-label="Map of post locations">
  <div id="locations-map" class="rounded-top shadow-sm border overflow-hidden" tabindex="0" style="height: min(60vh, 480px);"></div>

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
      {%- assign key = loc[0] -%}{%- assign posts = site.posts | where_exp: "p", "p.locations contains key" -%}
      {%- assign c_places = c_places | plus: 1 -%}{%- assign c_posts = c_posts | plus: posts.size -%}
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
            {%- assign key = loc[0] -%}
            {%- assign posts = site.posts | where_exp: "p", "p.locations contains key" -%}
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
      {%- assign posts = site.posts | where_exp: "p", "p.locations contains key" %}
      <li id="l-{{ key | slugify }}"><strong>{{ key }}</strong>: {% for post in posts %}<a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}</li>
    {%- endfor %}
    </ul>
  </div>
  {%- endif %}
</section>

</article>

<script>
(function () {
  // Same order as the list below: United States first, then countries A to Z.
  var places = [
  {%- for country in countries -%}{%- for loc in site.data.locations -%}{%- if loc[1].country == country -%}
    {%- assign key = loc[0] -%}
    {%- assign posts = site.posts | where_exp: "p", "p.locations contains key" %}
    { name: {{ loc[1].place | jsonify }}, region: {{ loc[1].region | jsonify }}, country: {{ loc[1].country | jsonify }}, lat: {{ loc[1].lat }}, lng: {{ loc[1].lng }}, anchor: "l-{{ loc[0] | slugify }}",
      posts: [{% for post in posts %}[{{ post.title | jsonify }}, {{ post.url | relative_url | jsonify }}, {{ post.date | date: "%b %Y" | jsonify }}]{% unless forloop.last %},{% endunless %}{% endfor %}] },
  {%- endif -%}{%- endfor -%}{%- endfor %}
  ];
  places.forEach(function (p) { p.where = p.region ? p.region + ", " + p.country : p.country; });

  // The map stays null until MapKit loads; the panel and the country list work without it.
  var map = null;
  var mapEl = document.getElementById("locations-map");

  function size(n) { return Math.round(22 + Math.sqrt(n) * 4); }
  function pin(label, s, classes) {
    var el = document.createElement("span");
    el.className = "loc-pin " + classes;
    el.style.width = el.style.height = s + "px";
    el.textContent = label;
    return el;
  }
  // MapKit positions the element it is given, so pins sit in a wrapper and keep their own hover and selected transforms.
  function annotationFor(coordinate, el, s, options) {
    options.anchorOffset = new DOMPoint(0, -s / 2); // MapKit anchors at the bottom center; this centers the circle on the place.
    options.size = { width: s, height: s };
    options.calloutEnabled = false;
    options.animates = false;
    return new mapkit.Annotation(coordinate, function () {
      var wrap = document.createElement("div");
      wrap.appendChild(el);
      return wrap;
    }, options);
  }
  // So the same pin can be selected again. MapKit ignores selection changes made inside a select handler.
  function deselectSoon(a) { setTimeout(function () { a.selected = false; }); }
  places.forEach(function (p) {
    p.pin = pin(p.posts.length, size(p.posts.length), "");
    p.pin.title = p.name + ", " + p.where;
  });

  window.initMapKit = function () {
    mapkit.addEventListener("error", function (e) {
      mapEl.innerHTML = '<p class="text-body-secondary small p-3 mb-0">The map could not load (' + esc(e.status) + '). The places are still listed below.</p>';
    });
    map = new mapkit.Map(mapEl);
    function applyTheme() {
      var dark = document.documentElement.getAttribute("data-bs-theme") === "dark";
      map.colorScheme = dark ? mapkit.Map.ColorSchemes.Dark : mapkit.Map.ColorSchemes.Light;
    }
    applyTheme();
    new MutationObserver(applyTheme).observe(document.documentElement, { attributes: true, attributeFilter: ["data-bs-theme"] });

    var padding = new mapkit.Padding(30, 30, 30, 30);
    // Nearby places merge into one circle showing their total posts; selecting it zooms in to split them.
    map.annotationForCluster = function (c) {
      var total = c.memberAnnotations.reduce(function (sum, a) { return sum + a.data.posts; }, 0);
      var s = size(total) + 6;
      var a = annotationFor(c.coordinate, pin(total, s, "loc-cluster"), s, { accessibilityLabel: total + " posts in " + c.memberAnnotations.length + " places" });
      a.addEventListener("select", function () {
        map.showItems(c.memberAnnotations, { animate: true, padding: padding });
        deselectSoon(a);
      });
      return a;
    };
    var annotations = places.map(function (p, i) {
      var s = size(p.posts.length);
      var a = annotationFor(new mapkit.Coordinate(p.lat, p.lng), p.pin, s, { clusteringIdentifier: "places", data: { posts: p.posts.length }, accessibilityLabel: p.pin.title });
      a.addEventListener("select", function () { select(i, false); deselectSoon(a); });
      return a;
    });
    map.showItems(annotations, { animate: false, padding: padding });
    if (zoomWhenReady) showOnMap(places[current]);
  };

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

  // Close enough that neighboring places in the Tri-Cities come apart. Not animated: MapKit drops a
  // new animated move while one is running, so quick arrow presses left the map behind the panel.
  function showOnMap(p) {
    map.region = new mapkit.CoordinateRegion(new mapkit.Coordinate(p.lat, p.lng), new mapkit.CoordinateSpan(0.3, 0.3));
  }

  // zoom: move the map to the place (stepping with the arrows); a click on the map leaves the view alone.
  var zoomWhenReady = false;
  function select(i, zoom) {
    if (current >= 0) places[current].pin.classList.remove("is-selected");
    current = (i + places.length) % places.length;
    places[current].pin.classList.add("is-selected");
    if (zoom) { if (map) showOnMap(places[current]); else zoomWhenReady = true; }
    panel.hidden = false;
    render(false);
  }

  more.addEventListener("click", function () { render(true); });
  panel.addEventListener("click", function (e) {
    var b = e.target.closest("[data-step]");
    if (b) select(current + Number(b.dataset.step), true);
  });
  [panel, mapEl].forEach(function (el) {
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
      mapEl.scrollIntoView({ behavior: "smooth", block: "center" });
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
<script src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js" crossorigin async data-callback="initMapKit" data-libraries="map,annotations" data-initial-token="{{ site.mapkit_token }}"></script>
