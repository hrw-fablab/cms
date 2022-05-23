// Function for handling Display of Submenus
document.addEventListener(
  "click",
  (event) => {
    if (event.target.dataset.type == "menu" && event.target.id != "menu-button") {
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
