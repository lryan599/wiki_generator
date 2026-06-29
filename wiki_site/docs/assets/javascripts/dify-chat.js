(function () {
  "use strict";

  var root = document.getElementById("dify-chat-root");
  if (!root) {
    return;
  }

  document.body.classList.add("dify-chat-page");
  renderDifyChat(root);

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

  function escapeAttribute(value) {
    return String(value || "#")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
})();
