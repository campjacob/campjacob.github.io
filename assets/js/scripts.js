---
---
// Various Scripts for Site

// Dictionary Scripts 
var myArray = [
	{% for term in site.dictionary %}
	"{{ term.title }}"{% unless forloop.last %},{% endunless %}
	{% endfor %}
];

var randomItem = myArray[Math.floor(Math.random()*myArray.length)];
//document.body.innerHTML = randomItem;
document.getElementById("RandomWord").innerHTML = "<a href='/dictionary/" + randomItem + "'>" + randomItem + "</a>";

// GLightbox Scripts
const lightbox = GLightbox({ selector: '.glightbox' });

document.addEventListener("DOMContentLoaded", function () {
// Select all <a> tags linking to image files
document.querySelectorAll('a[href$=".jpg"], a[href$=".jpeg"], a[href$=".png"], a[href$=".webp"], a[href$=".gif"]').forEach(link => {
  const img = link.querySelector('img');
  if (img) {
    link.classList.add('glightbox');
  }
});

GLightbox({ selector: '.glightbox' });
});

// Lunr Script

// lunr-site-search.js
// One script that supports BOTH:
// 1) Navbar dropdown search ( #navbar-search  +  #search-results )
// 2) Full search page ( #search-page-search  +  #search-page-results )
// Works even if one or the other is missing on a given page.

document.addEventListener("DOMContentLoaded", () => {
  const INDEX_URL = "/lunr-search.json";

  // -----------------------------
  // Shared index (loaded once)
  // -----------------------------
  let docs = [];
  let idx = null;
  let indexPromise = null;

  function loadIndexOnce() {
    if (indexPromise) return indexPromise;

    indexPromise = fetch(INDEX_URL, { cache: "no-store" })
      .then((r) => {
        if (!r.ok) throw new Error(`Failed to load ${INDEX_URL}: ${r.status}`);
        return r.json();
      })
      .then((json) => {
        docs = Array.isArray(json) ? json : [];

        idx = lunr(function () {
          this.ref("url");
          this.field("title", { boost: 10 });
          this.field("content");

          // Optional fields if present in your JSON (safe if missing)
          // this.field("type");
          // this.field("tags");

          docs.forEach((doc) => this.add(doc), this);
        });

        return { docs, idx };
      })
      .catch((err) => {
        console.error("Search index error:", err);
        docs = [];
        idx = null;
        throw err;
      });

    return indexPromise;
  }

  // -----------------------------
  // Helpers
  // -----------------------------
  function escapeHtml(str) {
    return (str || "").replace(/[&<>"']/g, (m) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    }[m]));
  }

  function safeSearch(query) {
    if (!idx) return [];
    // Lunr can throw on malformed query; fall back to a "tokenized" version.
    try {
      return idx.search(query);
    } catch (e) {
      const fallback = query
        .split(/\s+/)
        .filter(Boolean)
        .map((t) => `${t}*`)
        .join(" ");
      try {
        return idx.search(fallback);
      } catch {
        return [];
      }
    }
  }

  function resolveMatches(rawResults) {
    // Map lunr refs to docs (fast lookup)
    const byUrl = new Map(docs.map((d) => [d.url, d]));
    return rawResults
      .map((r) => byUrl.get(r.ref))
      .filter(Boolean);
  }

  function renderListItems(matches, { limit = 8 } = {}) {
    const slice = matches.slice(0, limit);

    if (!slice.length) {
      return `<li class="empty">No results</li>`;
    }

    return slice.map((item) => {
      const title = escapeHtml(item.title || item.url);
      const url = item.url; // expected already as a site-relative URL in your JSON

      const label = item.type
        ? `<span class="search-badge">[${escapeHtml(item.type)}]</span>`
        : "";

      const meta = item.date
        ? `<small class="text-muted ms-2">${escapeHtml(item.date)}</small>`
        : "";

      return `<li><a href="${url}">${label} ${title} ${meta}</a></li>`;
    }).join("");
  }

  // -----------------------------
  // NAVBAR SEARCH (dropdown)
  // Markup expected (your current):
  // #navbar-search contains:
  //   .search-toggle
  //   input#search-box
  //   ul#search-results
  // -----------------------------
  function initNavbarSearch() {
    const container = document.getElementById("navbar-search");
    if (!container) return;

    const toggleIcon = container.querySelector(".search-toggle");
    const input = container.querySelector("#search-box");
    const resultsEl = container.querySelector("#search-results");

    if (!toggleIcon || !input || !resultsEl) return;

    function showResultsHtml(html) {
      resultsEl.innerHTML = html;
      resultsEl.style.display = "block";
    }

    function hideResults() {
      resultsEl.style.display = "none";
      resultsEl.innerHTML = "";
    }

    // Toggle open/close
    toggleIcon.addEventListener("click", () => {
      container.classList.toggle("active");
      if (container.classList.contains("active")) {
        input.focus();
        // Lazy-load index on first open
        loadIndexOnce().catch(() => {
          showResultsHtml(`<li class="empty">Search unavailable</li>`);
        });
      } else {
        hideResults();
      }
    });

    // Close on Escape/outside click
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && container.classList.contains("active")) {
        container.classList.remove("active");
        hideResults();
        input.blur();
      }
    });

    document.addEventListener("click", (e) => {
      if (!container.contains(e.target)) {
        container.classList.remove("active");
        hideResults();
      }
    });

    // Live search
    input.addEventListener("input", async () => {
      const q = input.value.trim();
      if (!q) return hideResults();

      if (!idx) {
        showResultsHtml(`<li class="empty">Building search index…</li>`);
        try {
          await loadIndexOnce();
        } catch {
          return showResultsHtml(`<li class="empty">Search unavailable</li>`);
        }
      }

      const raw = safeSearch(q);
      const matches = resolveMatches(raw);
      showResultsHtml(renderListItems(matches, { limit: 8 }));
    });

    // Keyboard navigation in dropdown
    input.addEventListener("keydown", (e) => {
      if (resultsEl.style.display === "none") return;

      const links = Array.from(resultsEl.querySelectorAll("a"));
      if (!links.length) return;

      const current = document.activeElement;
      const i = links.indexOf(current);

      if (e.key === "ArrowDown") {
        e.preventDefault();
        (links[i + 1] || links[0]).focus();
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        (links[i - 1] || links[links.length - 1]).focus();
      }
    });
  }

  // -----------------------------
  // SEARCH PAGE
  // Recommended markup:
  // <input id="search-page-search" ...>
  // <ul id="search-page-results"></ul>
  //
  // (This avoids ID conflicts with the navbar #search-box.)
  // -----------------------------
  function initSearchPage() {
    const input = document.getElementById("search-page-search");
    const resultsEl = document.getElementById("search-page-results");
    if (!input || !resultsEl) return;

    function setResults(html) {
      resultsEl.innerHTML = html;
    }

    // Load index immediately on the search page for snappy UX
    loadIndexOnce()
      .then(() => {
        // If you support ?q= in URL, auto-run it
        const params = new URLSearchParams(window.location.search);
        const q = (params.get("q") || "").trim();
        if (q) {
          input.value = q;
          const raw = safeSearch(q);
          const matches = resolveMatches(raw);
          setResults(renderListItems(matches, { limit: 50 }));
        }
      })
      .catch(() => {
        setResults(`<li class="empty">Search unavailable</li>`);
      });

    input.addEventListener("input", () => {
      const q = input.value.trim();
      if (!q) return setResults("");

      const raw = safeSearch(q);
      const matches = resolveMatches(raw);
      setResults(renderListItems(matches, { limit: 50 }));
    });
  }

  // -----------------------------
  // Boot
  // -----------------------------
  initNavbarSearch();
  initSearchPage();
});