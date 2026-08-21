// Shared nav + footer for cyber.cashlessconsumer.in (GitHub Pages static).

// Mark the current page's nav link as active.
document.addEventListener("DOMContentLoaded", () => {
  const here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.links a").forEach((a) => {
    const target = a.getAttribute("href").split("/").pop();
    if (target === here || (here === "" && target === "index.html")) {
      a.classList.add("active");
    }
  });

  // Mobile nav toggle.
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector("nav.links");
  if (toggle && links) {
    toggle.addEventListener("click", () => links.classList.toggle("open"));
    links.addEventListener("click", (e) => {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }
});
