// Live Apple Maps for FitPub activities, on /stream/ and each activity's own page.
// Cards carry the route in data-track (see _includes/stream-card.htm). FitPub's route image stays
// in the markup as the fallback for embeds and for when MapKit can't load.
//
// A map exists only while its card is near the screen: browsers limit how many live maps a page
// can hold, and Apple's allowance counts map views. Maps in the list don't pan or zoom, so they
// never trap scrolling on a phone; selecting one opens the activity's own page.
(function () {
  var root = document.documentElement;
  var active = new Set();
  var observer = null;
  window.initActivityMaps = function () {};
  window.activityMapsFailed = function () {};
  if (root.classList.contains("embed")) return; // Embeds keep the image.

  root.classList.add("activity-maps"); // Hides the images (foundation.css) so they don't flash first.

  function applyTheme(map) {
    var dark = root.getAttribute("data-bs-theme") === "dark";
    map.colorScheme = dark ? mapkit.Map.ColorSchemes.Dark : mapkit.Map.ColorSchemes.Light;
  }

  function line(points, color, width) {
    return new mapkit.PolylineOverlay(points, { style: new mapkit.Style({ strokeColor: color, lineWidth: width, lineCap: "round", lineJoin: "round" }) });
  }

  function dot(coordinate, color, label) {
    return new mapkit.Annotation(coordinate, function () {
      var el = document.createElement("div");
      el.style.cssText = "width: 14px; height: 14px; box-sizing: border-box; border-radius: 50%; border: 2px solid #fff; background: " + color + ";";
      el.title = label;
      return el;
    }, { anchorOffset: new DOMPoint(0, -7), size: { width: 14, height: 14 }, calloutEnabled: false, animates: false, accessibilityLabel: label });
  }

  function build(box) {
    var interactive = box.dataset.interactive === "true";
    var layer = document.createElement("div");
    layer.className = "activity-map-layer";
    var mapEl = document.createElement("div");
    mapEl.className = "activity-map";
    layer.appendChild(mapEl);
    box.appendChild(layer);

    var options = { pointOfInterestFilter: mapkit.PointOfInterestFilter.excludingAllCategories };
    if (!interactive) {
      options.isScrollEnabled = options.isZoomEnabled = options.isRotationEnabled = false;
      options.showsZoomControl = options.showsMapTypeControl = false;
      options.showsCompass = mapkit.FeatureVisibility.Hidden;
    }
    var map = new mapkit.Map(mapEl, options);
    applyTheme(map);

    var segments = JSON.parse(box.dataset.track).map(function (part) {
      return part.map(function (p) { return new mapkit.Coordinate(p[1], p[0]); });
    });
    var lines = [];
    segments.forEach(function (points) { lines.push(line(points, "#fff", 7), line(points, "#fd7e14", 4)); });
    map.addOverlays(lines);
    var last = segments[segments.length - 1];
    var dots = [dot(segments[0][0], "#198754", "Start"), dot(last[last.length - 1], "#212529", "Finish")];
    map.addAnnotations(dots);
    map.showItems(lines.concat(dots), { animate: false, padding: new mapkit.Padding(30, 30, 30, 30) });

    if (box.dataset.label) {
      var label = document.createElement("div");
      label.className = "activity-map-label";
      label.textContent = box.dataset.label;
      layer.appendChild(label);
    }
    if (!interactive) {
      var link = document.createElement("a");
      link.className = "activity-map-link";
      link.href = box.dataset.url;
      link.setAttribute("aria-label", "Open this activity");
      layer.appendChild(link);
    }
    box.activityMap = { map: map, layer: layer };
    active.add(box);
  }

  function teardown(box) {
    box.activityMap.map.destroy();
    box.activityMap.layer.remove();
    box.activityMap = null;
    active.delete(box);
  }

  window.activityMapsFailed = function () {
    if (observer) observer.disconnect();
    active.forEach(teardown);
    root.classList.remove("activity-maps");
  };

  window.initActivityMaps = function () {
    mapkit.addEventListener("error", window.activityMapsFailed);
    new MutationObserver(function () {
      active.forEach(function (box) { applyTheme(box.activityMap.map); });
    }).observe(root, { attributes: true, attributeFilter: ["data-bs-theme"] });
    observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && !e.target.activityMap) build(e.target);
        else if (!e.isIntersecting && e.target.activityMap) teardown(e.target);
      });
    }, { rootMargin: "400px 0px" });
    document.querySelectorAll(".stream-activity[data-track]").forEach(function (box) { observer.observe(box); });
  };
})();
