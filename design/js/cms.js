// Function for handling Display of Submenus
document.addEventListener(
  "click",
  (event) => {
    if (
      event.target.dataset.type == "menu" &&
      event.target.id != "menu-button" &&
      event.target.nextElementSibling.classList.contains("hidden")
    ) {
      for (element of document.querySelectorAll('[data-menu="submenu"]')) {
        element.classList.add("hidden");
      }
      return event.target.nextElementSibling.classList.toggle("hidden");
    }
    for (element of document.querySelectorAll('[data-menu="submenu"]')) {
      element.classList.add("hidden");
    }
  },
  { passive: true }
);

// Function to handle Display of Menu on Mobile Navigation
document.getElementById("menu-button").addEventListener(
  "click",
  (event) => {
    if (getComputedStyle(event.target.nextElementSibling).display === "none") {
      event.target.nextElementSibling.style.display = "flex";
      document.getElementById("search").style.display = "flex";
      return;
    }
    event.target.nextElementSibling.style.display = "none";
    document.getElementById("search").style.display = "none";
  },
  { passive: true }
);

const callback = (entries, observer) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add("fade-in");
        observer.unobserve(entry.target);
      }, index * 100);
    }
  });
};

const cardObserver = new IntersectionObserver(callback, {});
const mediaObserver = new IntersectionObserver(callback, {});

const cardsElements = document
  .querySelectorAll(".card")
  .forEach((x) => cardObserver.observe(x));

const iframeElements = document
  .querySelectorAll("iframe")
  .forEach((x) => mediaObserver.observe(x));
