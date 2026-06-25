(function () {
  "use strict";

  var difyRoot = document.getElementById("dify-chat-root");
  if (difyRoot) {
    document.body.classList.add("wiki-assistant-page", "dify-chat-page");
    renderDifyChat(difyRoot);
    return;
  }

  var root = document.getElementById("wiki-assistant-root");
  if (!root) {
    return;
  }

  document.body.classList.add("wiki-assistant-page");

  var state = {
    mode: "auto",
    busy: false,
    messages: [],
    wikiResults: [],
    evidence: [],
    apiBase: localStorage.getItem("wikiAssistantApiBase") || "",
  };

  var examples = [
    "压铸模热疲劳裂纹怎么预防？",
    "H13钢热处理对模具寿命有什么影响？",
    "冷隔缺陷通常由哪些因素造成？",
  ];

  var steps = [
    ["intent", "理解问题"],
    ["wiki", "搜索 Wiki"],
    ["deep", "补充资料"],
    ["answer", "生成回答"],
  ];

  root.innerHTML =
    '<section class="wiki-assistant-shell">' +
    '  <header class="wiki-assistant-hero">' +
    '    <div>' +
    '      <div class="wiki-assistant-kicker">Wiki Assistant</div>' +
    '      <h2>智能问答</h2>' +
    "    </div>" +
    '    <div class="wiki-assistant-hero-tags" aria-label="检索能力">' +
    '      <span>Wiki 优先</span>' +
    '      <span>二级检索</span>' +
    '      <span>引用追踪</span>' +
    "    </div>" +
    "  </header>" +
    '<div class="wiki-assistant">' +
    '  <div class="wiki-assistant-main">' +
    '    <section class="wiki-assistant-composer">' +
    '      <div class="wiki-assistant-toolbar">' +
    '      <div class="wiki-assistant-mode" role="tablist" aria-label="搜索模式">' +
    '        <button type="button" data-mode="auto" class="is-active">自动</button>' +
    '        <button type="button" data-mode="search">搜 Wiki</button>' +
    '        <button type="button" data-mode="deep">深度</button>' +
    '        <button type="button" data-mode="answer">回答</button>' +
    "      </div>" +
    '      <div class="wiki-assistant-config">' +
    '        <input type="url" data-api-base placeholder="API 地址" aria-label="API 地址">' +
    '        <button type="button" class="wiki-assistant-icon-button" data-save-api title="保存 API 地址" aria-label="保存 API 地址"><span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span></button>' +
    "      </div>" +
    "      </div>" +
    '      <form class="wiki-assistant-query" data-query-form>' +
    '        <textarea data-query-input placeholder="输入问题，例如：压铸模热疲劳裂纹怎么预防？" aria-label="问题"></textarea>' +
    '        <div class="wiki-assistant-query-footer">' +
    '          <div class="wiki-assistant-examples" data-examples></div>' +
    '          <button type="submit" class="wiki-assistant-send" data-send aria-label="发送"><span class="glyphicon glyphicon-send" aria-hidden="true"></span><span>发送</span></button>' +
    "        </div>" +
    "      </form>" +
    "    </section>" +
    '    <div class="wiki-assistant-status" data-status></div>' +
    '    <div class="wiki-assistant-thread" data-thread></div>' +
    "  </div>" +
    '  <aside class="wiki-assistant-side">' +
    '    <section class="wiki-assistant-panel">' +
    '      <div class="wiki-assistant-panel-header"><span>相关条目</span><span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span></div>' +
    '      <div class="wiki-assistant-panel-body" data-side-results></div>' +
    "    </section>" +
    '    <section class="wiki-assistant-panel">' +
    '      <div class="wiki-assistant-panel-header"><span>引用证据</span><span class="glyphicon glyphicon-link" aria-hidden="true"></span></div>' +
    '      <div class="wiki-assistant-panel-body" data-side-evidence></div>' +
    "    </section>" +
    "  </aside>" +
    "</div>" +
    "</section>";

  var elements = {
    form: root.querySelector("[data-query-form]"),
    input: root.querySelector("[data-query-input]"),
    send: root.querySelector("[data-send]"),
    apiBase: root.querySelector("[data-api-base]"),
    saveApi: root.querySelector("[data-save-api]"),
    modeButtons: Array.prototype.slice.call(root.querySelectorAll("[data-mode]")),
    examples: root.querySelector("[data-examples]"),
    status: root.querySelector("[data-status]"),
    thread: root.querySelector("[data-thread]"),
    sideResults: root.querySelector("[data-side-results]"),
    sideEvidence: root.querySelector("[data-side-evidence]"),
  };

  elements.apiBase.value = state.apiBase;

  examples.forEach(function (text) {
    var button = document.createElement("button");
    button.type = "button";
    button.textContent = text;
    button.addEventListener("click", function () {
      elements.input.value = text;
      elements.input.focus();
    });
    elements.examples.appendChild(button);
  });

  elements.modeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      state.mode = button.getAttribute("data-mode") || "auto";
      elements.modeButtons.forEach(function (item) {
        item.classList.toggle("is-active", item === button);
      });
    });
  });

  elements.saveApi.addEventListener("click", function () {
    state.apiBase = elements.apiBase.value.trim().replace(/\/+$/, "");
    localStorage.setItem("wikiAssistantApiBase", state.apiBase);
    addSystemMessage("API 地址已保存。");
  });

  elements.form.addEventListener("submit", function (event) {
    event.preventDefault();
    submitQuery();
  });

  renderStatus();
  renderThread();
  renderSidebars();

  async function submitQuery() {
    var query = elements.input.value.trim();
    if (!query || state.busy) {
      return;
    }

    state.busy = true;
    state.wikiResults = [];
    state.evidence = [];
    state.messages.push({
      role: "user",
      title: "你",
      body: escapeHtml(query),
    });
    renderAll("intent");

    try {
      setActiveStep("wiki");
      var response = await requestAssistant(query);
      state.wikiResults = normalizeResults(response.wiki_results || response.wikiResults || []);
      state.evidence = normalizeEvidence(response.evidence || []);
      state.messages.push({
        role: "assistant",
        title: response.mode === "search" ? "搜索结果" : "智能问答",
        body: renderAnswer(response.answer, response.fallback_message),
        results: state.wikiResults,
      });
      renderAll("answer", true);
    } catch (error) {
      setActiveStep("wiki");
      var fallback = await localSearch(query);
      state.wikiResults = fallback;
      state.evidence = [];
      state.messages.push({
        role: "assistant",
        title: "本地索引",
        body:
          '<div class="wiki-assistant-alert">后端暂未连接，已切换为 MkDocs 本地索引。</div>',
        results: fallback,
      });
      renderAll("answer", true);
    } finally {
      state.busy = false;
      elements.send.disabled = false;
    }
  }

  async function requestAssistant(query) {
    var apiBase = state.apiBase || window.WIKI_ASSISTANT_API_BASE || "";
    var url = apiBase.replace(/\/+$/, "") + "/api/wiki-assistant/query";
    var response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: query,
        mode: state.mode,
        top_k: 5,
        stream: false,
      }),
    });

    if (!response.ok) {
      throw new Error("Assistant API returned " + response.status);
    }

    return response.json();
  }

  async function localSearch(query) {
    var indexUrl = getBasePath() + "search/search_index.json";
    var response = await fetch(indexUrl);
    if (!response.ok) {
      return [];
    }
    var data = await response.json();
    var docs = data.docs || [];
    var terms = buildQueryTerms(query);
    var cjkChars = uniqueCjkChars(query);

    return docs
      .map(function (doc) {
        var haystack = ((doc.title || "") + " " + (doc.text || "")).toLowerCase();
        var score = scoreLocalDocument(haystack, terms, cjkChars);
        return {
          title: doc.title || doc.location || "未命名条目",
          url: getBasePath() + doc.location,
          section: "",
          snippet: "",
          snippetHtml: makeSnippet(doc.text || "", terms.concat(cjkChars)),
          score: score,
          source: "mkdocs",
        };
      })
      .filter(function (item) {
        return item.score > 0;
      })
      .sort(function (a, b) {
        return b.score - a.score;
      })
      .slice(0, 6);
  }

  function buildQueryTerms(query) {
    var lower = String(query || "").toLowerCase();
    var splitTerms = lower.split(/[\s,，。；;、！？!?：:（）()]+/).filter(Boolean);
    var latinTerms = lower.match(/[a-z0-9][a-z0-9.+#_-]*/g) || [];
    return unique(splitTerms.concat(latinTerms)).filter(function (term) {
      return term.length >= 2;
    });
  }

  function uniqueCjkChars(query) {
    return unique((String(query || "").match(/[\u3400-\u9fff]/g) || []));
  }

  function scoreLocalDocument(haystack, terms, cjkChars) {
    var score = terms.reduce(function (total, term) {
      return total + (haystack.indexOf(term) >= 0 ? Math.max(2, term.length) : 0);
    }, 0);
    if (cjkChars.length) {
      var hits = cjkChars.reduce(function (total, char) {
        return total + (haystack.indexOf(char) >= 0 ? 1 : 0);
      }, 0);
      score += hits / cjkChars.length;
    }
    return Math.round(score * 100) / 100;
  }

  function unique(items) {
    return items.filter(function (item, index) {
      return item && items.indexOf(item) === index;
    });
  }

  function normalizeResults(results) {
    return results.map(function (item) {
      return {
        title: item.title || item.name || "未命名条目",
        url: item.url || item.path || "#",
        section: item.section || item.heading || "",
        snippet: item.snippet || item.content || item.summary || "",
        snippetHtml: item.snippet_html || item.snippetHtml || "",
        score: typeof item.score === "number" ? item.score : null,
        source: item.workspace || item.source || "wiki",
      };
    });
  }

  function normalizeEvidence(items) {
    return items.map(function (item) {
      return {
        title: item.title || item.name || item.workspace || "证据",
        content: item.content || item.summary || item.caption || item.body || "",
        url: item.url || "",
        source: item.workspace || item.source_type || "",
      };
    });
  }

  function renderAnswer(answer, fallbackMessage) {
    if (answer) {
      return markdownLite(String(answer));
    }
    return (
      '<div class="wiki-assistant-alert">' +
      escapeHtml(fallbackMessage || "已返回相关文档，生成式回答等待后端接入。") +
      "</div>"
    );
  }

  function addSystemMessage(text) {
    state.messages.push({
      role: "assistant",
      title: "设置",
      body: '<div class="wiki-assistant-alert">' + escapeHtml(text) + "</div>",
    });
    renderThread();
  }

  function renderAll(activeStep, done) {
    elements.send.disabled = state.busy;
    renderStatus(activeStep, done);
    renderThread();
    renderSidebars();
  }

  function setActiveStep(step) {
    renderStatus(step);
  }

  function renderStatus(activeStep, done) {
    elements.status.innerHTML = "";
    steps.forEach(function (step) {
      var node = document.createElement("span");
      node.className = "wiki-assistant-step";
      if (activeStep === step[0]) {
        node.classList.add("is-active");
      }
      if (done) {
        node.classList.add("is-done");
      }
      node.innerHTML =
        '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span>' +
        escapeHtml(step[1]);
      elements.status.appendChild(node);
    });
  }

  function renderThread() {
    elements.thread.innerHTML = "";
    if (!state.messages.length) {
      var empty = document.createElement("div");
      empty.className = "wiki-assistant-message";
      empty.innerHTML =
        '<div class="wiki-assistant-message-header"><span>智能问答</span><span>待机</span></div>' +
        '<div class="wiki-assistant-message-body"><p>等待输入。</p></div>';
      elements.thread.appendChild(empty);
      return;
    }

    state.messages.forEach(function (message) {
      var node = document.createElement("article");
      node.className = "wiki-assistant-message";
      node.setAttribute("data-role", message.role);
      node.innerHTML =
        '<div class="wiki-assistant-message-header"><span>' +
        escapeHtml(message.title) +
        "</span><span>" +
        (message.role === "user" ? "Query" : "Result") +
        "</span></div>" +
        '<div class="wiki-assistant-message-body">' +
        message.body +
        "</div>";

      if (message.results && message.results.length) {
        node.appendChild(renderResults(message.results));
      }
      elements.thread.appendChild(node);
    });
  }

  function renderResults(results) {
    var wrapper = document.createElement("div");
    wrapper.className = "wiki-assistant-results";
    results.forEach(function (item) {
      var row = document.createElement("div");
      row.className = "wiki-assistant-result";
      row.innerHTML =
        '<div class="wiki-assistant-result-title"><a href="' +
        escapeAttribute(item.url) +
        '">' +
        escapeHtml(item.title) +
        '</a><span class="wiki-assistant-result-meta">' +
        formatScore(item.score) +
        "</span></div>" +
        '<div class="wiki-assistant-result-meta">' +
        escapeHtml([item.section, item.source].filter(Boolean).join(" · ")) +
        "</div>" +
        '<div class="wiki-assistant-result-snippet">' +
        renderSnippet(item) +
        "</div>";
      wrapper.appendChild(row);
    });
    return wrapper;
  }

  function renderSnippet(item) {
    if (item.snippetHtml) {
      return item.snippetHtml;
    }
    return markdownLite(item.snippet || "");
  }

  function renderSidebars() {
    elements.sideResults.innerHTML = "";
    elements.sideEvidence.innerHTML = "";

    if (!state.wikiResults.length) {
      elements.sideResults.innerHTML = '<div class="wiki-assistant-empty">暂无条目。</div>';
    } else {
      state.wikiResults.slice(0, 5).forEach(function (item) {
        var node = document.createElement("div");
        node.className = "wiki-assistant-citation";
        node.innerHTML =
          '<div class="wiki-assistant-citation-title"><a href="' +
          escapeAttribute(item.url) +
          '">' +
          escapeHtml(item.title) +
          "</a></div>" +
          '<div class="wiki-assistant-citation-content">' +
          escapeHtml(item.section || item.source || "") +
          "</div>";
        elements.sideResults.appendChild(node);
      });
    }

    if (!state.evidence.length) {
      elements.sideEvidence.innerHTML = '<div class="wiki-assistant-empty">暂无证据。</div>';
    } else {
      state.evidence.slice(0, 6).forEach(function (item) {
        var node = document.createElement("div");
        node.className = "wiki-assistant-citation";
        var title = item.url
          ? '<a href="' + escapeAttribute(item.url) + '">' + escapeHtml(item.title) + "</a>"
          : escapeHtml(item.title);
        node.innerHTML =
          '<div class="wiki-assistant-citation-title">' +
          title +
          "</div>" +
          '<div class="wiki-assistant-citation-content">' +
          escapeHtml(shorten(item.content, 180)) +
          "</div>";
        elements.sideEvidence.appendChild(node);
      });
    }
  }

  function makeSnippet(text, terms) {
    var clean = String(text || "").replace(/\s+/g, " ").trim();
    if (!clean) {
      return "";
    }
    var lower = clean.toLowerCase();
    var position = 0;
    for (var i = 0; i < terms.length; i += 1) {
      var found = lower.indexOf(terms[i]);
      if (found >= 0) {
        position = Math.max(0, found - 72);
        break;
      }
    }
    return highlight(clean.slice(position, position + 220), terms);
  }

  function highlight(text, terms) {
    var escaped = escapeHtml(text);
    terms.forEach(function (term) {
      if (!term || /[.*+?^${}()|[\]\\]/.test(term)) {
        return;
      }
      escaped = escaped.replace(new RegExp("(" + term + ")", "gi"), "<mark>$1</mark>");
    });
    return escaped;
  }

  function markdownLite(text) {
    return escapeHtml(String(text || ""))
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n{2,}/g, "</p><p>")
      .replace(/\n/g, "<br>")
      .replace(/^/, "<p>")
      .replace(/$/, "</p>");
  }

  function getBasePath() {
    var link = document.querySelector('link[href$="css/base.css"]');
    if (!link) {
      return "/";
    }
    return link.getAttribute("href").replace(/css\/base\.css$/, "");
  }

  function formatScore(score) {
    if (typeof score !== "number") {
      return "";
    }
    if (score <= 1) {
      return Math.round(score * 100) + "%";
    }
    return String(score);
  }

  function shorten(text, limit) {
    var clean = String(text || "").replace(/\s+/g, " ").trim();
    if (clean.length <= limit) {
      return clean;
    }
    return clean.slice(0, limit - 1) + "...";
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function escapeAttribute(value) {
    return escapeHtml(value || "#");
  }

  function renderDifyChat(container) {
    var src = container.getAttribute("data-dify-src") || "";
    container.innerHTML =
      '<section class="dify-chat-shell">' +
      '  <div class="dify-chat-frame-wrap">' +
      '    <iframe src="' +
      escapeAttribute(src) +
      '" class="dify-chat-frame" frameborder="0" allow="microphone"></iframe>' +
      "  </div>" +
      "</section>";
  }
})();
