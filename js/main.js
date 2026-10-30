// Shared nav behavior for cyber.cashlessconsumer.in (GitHub Pages static).
// Disclosure-pattern dropdowns + mobile hamburger. No dependencies.
(function () {
  // Mark the current page's nav link as active (and expose it to AT).
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.links a").forEach(function (a) {
    var target = a.getAttribute("href").split("/").pop();
    if (target === here) {
      a.classList.add("active");
      a.setAttribute("aria-current", "page");
      // Light up the group button that contains the current page.
      var menu = a.closest(".menu");
      if (menu) menu.querySelector(".menu-btn").classList.add("current");
    }
  });

  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector("nav.links");
  if (!toggle || !links) return;

  var menus = Array.prototype.slice.call(document.querySelectorAll(".menu"));

  function closeMenu(menu) {
    menu.classList.remove("open");
    var btn = menu.querySelector(".menu-btn");
    if (btn) btn.setAttribute("aria-expanded", "false");
  }
  function closeMenus() { menus.forEach(closeMenu); }
  function setNav(open) {
    links.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    if (!open) closeMenus();
  }

  // Group disclosure buttons.
  menus.forEach(function (menu) {
    var btn = menu.querySelector(".menu-btn");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = !menu.classList.contains("open");
      closeMenus();
      menu.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close when keyboard focus leaves the group.
    menu.addEventListener("focusout", function (e) {
      if (!menu.contains(e.relatedTarget)) closeMenu(menu);
    });
  });

  // Mobile nav toggle.
  toggle.addEventListener("click", function () {
    setNav(!links.classList.contains("open"));
  });

  // Choosing a link collapses everything.
  links.addEventListener("click", function (e) {
    if (e.target.closest("a")) setNav(false);
  });

  // Escape: close the open menu first, else the mobile panel.
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var openMenu = document.querySelector(".menu.open");
    if (openMenu) {
      closeMenu(openMenu);
      var btn = openMenu.querySelector(".menu-btn");
      if (btn) btn.focus();
    } else if (links.classList.contains("open")) {
      setNav(false);
      toggle.focus();
    }
  });

  // Click outside the header collapses everything.
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".topbar")) {
      closeMenus();
      if (links.classList.contains("open")) setNav(false);
    }
  });
})();
