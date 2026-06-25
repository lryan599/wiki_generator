(function () {
  "use strict";

  var batchSize = 200;

  function getBasePath() {
    var value = typeof base_url !== "undefined" ? base_url : ".";
    return value.replace(/\/+$/, "") || ".";
  }

  function toSiteUrl(location) {
    var basePath = getBasePath();
    return basePath + "/" + location.replace(/^\/+/, "");
  }

  function normalizeUrl(url) {
    try {
      url = decodeURI(url);
    } catch (error) {
      // Keep the original URL if the browser cannot decode it.
    }
    return url
      .split("#")[0]
      .split("?")[0]
      .replace(/\/index\.html$/, "/")
      .replace(/\/$/, "");
  }

  function entrySortKey(title) {
    return title.toLowerCase();
  }

  function normalizeEntry(entry) {
    if (Array.isArray(entry)) {
      return {
        title: entry[0],
        location: entry[1],
      };
    }
    return {
      title: entry.title,
      location: entry.location,
    };
  }

  function uniqueEntries(entries) {
    var seen = {};
    var normalizedEntries = [];

    entries.forEach(function (entry) {
      var normalizedEntry = normalizeEntry(entry);
      var title = normalizedEntry.title;
      var location = normalizedEntry.location;

      if (!title || !location || location.indexOf("entries/") !== 0) {
        return;
      }

      var normalized = location.replace(/\/?$/, "/");
      if (seen[normalized]) {
        return;
      }

      seen[normalized] = true;
      normalizedEntries.push({
        title: title,
        location: normalized,
        searchText: (title + " " + normalized).toLowerCase(),
      });
    });

    normalizedEntries.sort(function (left, right) {
      var leftKey = entrySortKey(left.title);
      var rightKey = entrySortKey(right.title);
      return leftKey.localeCompare(rightKey, "zh-Hans-CN");
    });

    return normalizedEntries;
  }

  function prioritizeCurrentEntry(entries, currentUrl) {
    var currentIndex = entries.findIndex(function (entry) {
      var href = toSiteUrl(entry.location);
      return normalizeUrl(new URL(href, window.location.href).href) === currentUrl;
    });

    if (currentIndex <= 0) {
      return entries;
    }

    var copy = entries.slice();
    var currentEntry = copy.splice(currentIndex, 1)[0];
    copy.unshift(currentEntry);
    return copy;
  }

  function renderEntryDrawer(entries) {
    if (!document.body || document.getElementById("wiki-entry-drawer")) {
      return;
    }

    var chatHref = toSiteUrl("chat/");
    var chatIsActive =
      normalizeUrl(new URL(chatHref, window.location.href).href) ===
      normalizeUrl(window.location.href);
    var shell = document.createElement("div");
    shell.className = "wiki-entry-drawer-shell";
    shell.innerHTML =
      '<div class="wiki-floating-actions">' +
      '<button type="button" class="wiki-entry-drawer-toggle" aria-controls="wiki-entry-drawer" aria-expanded="false">' +
      '  <span class="fa fa-list-ul" aria-hidden="true"></span>' +
      "  <span>条目</span>" +
      "</button>" +
      '<a class="wiki-assistant-shortcut' +
      (chatIsActive ? " is-active" : "") +
      '" href="' +
      chatHref +
      '"' +
      (chatIsActive ? ' aria-current="page"' : "") +
      ">" +
      '  <span class="fa fa-comments" aria-hidden="true"></span>' +
      "  <span>智能问答</span>" +
      "</a>" +
      "</div>" +
      '<div class="wiki-entry-drawer-backdrop" data-entry-drawer-close></div>' +
      '<aside id="wiki-entry-drawer" class="wiki-entry-drawer" aria-hidden="true">' +
      '  <div class="wiki-entry-nav-title-row">' +
      '    <div class="wiki-entry-nav-title">Wiki 条目</div>' +
      '    <div class="wiki-entry-drawer-actions">' +
      '      <div class="wiki-entry-nav-count"></div>' +
      '      <button type="button" class="wiki-entry-drawer-close" data-entry-drawer-close aria-label="关闭条目栏">' +
      '        <span class="fa fa-times" aria-hidden="true"></span>' +
      "      </button>" +
      "    </div>" +
      "  </div>" +
      '  <div class="wiki-entry-nav-tools">' +
      '    <input type="search" class="wiki-entry-nav-search" placeholder="筛选条目" aria-label="筛选条目">' +
      "  </div>" +
      '  <div class="wiki-entry-nav-scroll">' +
      '    <ul class="nav flex-column wiki-entry-nav-list"></ul>' +
      '    <button type="button" class="wiki-entry-nav-more">显示更多</button>' +
      '    <div class="wiki-entry-nav-empty">没有匹配的条目</div>' +
      "  </div>" +
      "</aside>";
    document.body.appendChild(shell);

    var current = normalizeUrl(window.location.href);
    var allEntries = prioritizeCurrentEntry(uniqueEntries(entries), current);
    var filteredEntries = allEntries;
    var renderedCount = 0;
    var drawer = shell.querySelector(".wiki-entry-drawer");
    var toggle = shell.querySelector(".wiki-entry-drawer-toggle");
    var count = shell.querySelector(".wiki-entry-nav-count");
    var search = shell.querySelector(".wiki-entry-nav-search");
    var scroll = shell.querySelector(".wiki-entry-nav-scroll");
    var list = shell.querySelector(".wiki-entry-nav-list");
    var more = shell.querySelector(".wiki-entry-nav-more");
    var empty = shell.querySelector(".wiki-entry-nav-empty");

    function updateCount() {
      count.textContent = filteredEntries.length + " 条";
    }

    function renderMore() {
      var end = Math.min(renderedCount + batchSize, filteredEntries.length);
      var fragment = document.createDocumentFragment();

      for (var index = renderedCount; index < end; index += 1) {
        var entry = filteredEntries[index];
        var href = toSiteUrl(entry.location);
        var item = document.createElement("li");
        var link = document.createElement("a");

        item.className = "nav-item";
        link.className = "nav-link";
        link.href = href;
        link.textContent = entry.title;

        if (normalizeUrl(new URL(href, window.location.href).href) === current) {
          link.classList.add("active");
          link.setAttribute("aria-current", "page");
        }

        item.appendChild(link);
        fragment.appendChild(item);
      }

      list.appendChild(fragment);
      renderedCount = end;
      more.hidden = renderedCount >= filteredEntries.length;
      empty.hidden = filteredEntries.length !== 0;
    }

    function resetList(nextEntries) {
      filteredEntries = nextEntries;
      renderedCount = 0;
      list.textContent = "";
      scroll.scrollTop = 0;
      updateCount();
      renderMore();
    }

    function applyFilter() {
      var query = search.value.trim().toLowerCase();
      if (!query) {
        resetList(allEntries);
        return;
      }

      resetList(
        allEntries.filter(function (entry) {
          return entry.searchText.indexOf(query) !== -1;
        })
      );
    }

    search.addEventListener("input", applyFilter);
    more.addEventListener("click", renderMore);
    scroll.addEventListener("scroll", function () {
      if (scroll.scrollTop + scroll.clientHeight >= scroll.scrollHeight - 80) {
        renderMore();
      }
    });
    shell.addEventListener("click", function (event) {
      if (event.target.closest("[data-entry-drawer-close]")) {
        closeDrawer();
      }
    });
    toggle.addEventListener("click", function () {
      if (document.body.classList.contains("wiki-entry-drawer-open")) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeDrawer();
      }
    });

    function openDrawer() {
      document.body.classList.add("wiki-entry-drawer-open");
      drawer.setAttribute("aria-hidden", "false");
      toggle.setAttribute("aria-expanded", "true");
      window.setTimeout(function () {
        search.focus();
      }, 120);
    }

    function closeDrawer() {
      document.body.classList.remove("wiki-entry-drawer-open");
      drawer.setAttribute("aria-hidden", "true");
      toggle.setAttribute("aria-expanded", "false");
    }

    resetList(allEntries);
  }

  async function loadEntries() {
    var indexUrl = toSiteUrl("assets/data/wiki-entries.json");
    try {
      var response = await fetch(indexUrl, { cache: "no-store" });
      if (!response.ok) {
        throw new Error("wiki entry manifest unavailable");
      }
      var index = await response.json();
      renderEntryDrawer(index.entries || []);
    } catch (error) {
      renderEntryDrawer([]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadEntries);
  } else {
    loadEntries();
  }
})();
