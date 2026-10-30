// Shared nav behavior for cyber.cashlessconsumer.in (GitHub Pages static).
(function () {
  // Mark the current page's nav link as active (and expose it to AT).
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.links a").forEach(function (a) {
    var target = a.getAttribute("href").split("/").pop();
    if (target === here) {
      a.classList.add("active");
      a.setAttribute("aria-current", "page");
    }
  });

  // Mobile nav toggle with correct state semantics.
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector("nav.links");
  if (!toggle || !links) return;

  function setNav(open) {
    links.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  toggle.addEventListener("click", function () {
    setNav(!links.classList.contains("open"));
  });

  // Close after choosing a link.
  links.addEventListener("click", function (e) {
    if (e.target.closest("a")) setNav(false);
  });

  // Escape closes and returns focus to the toggle.
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && links.classList.contains("open")) {
      setNav(false);
      toggle.focus();
    }
  });

  // Click outside the header closes it.
  document.addEventListener("click", function (e) {
    if (links.classList.contains("open") && !e.target.closest(".topbar")) {
      setNav(false);
    }
  });
})();
