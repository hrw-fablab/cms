// Function for handling Display of Submenus
document.addEventListener(
  "click",
  (event) => {
    if (event.target.tagName == "BUTTON" && event.target.id != "menu-button") {
      if (
        getComputedStyle(event.target.nextElementSibling).display === "none"
      ) {
        for (element of document.getElementsByClassName("fl-submenu")) {
          element.classList.add("hidden");
        }
        return event.target.nextElementSibling.classList.remove("hidden");
      }
      return event.target.nextElementSibling.classList.add("hidden");
    }
    for (element of document.getElementsByClassName("fl-submenu")) {
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
      document.getElementById("settings").style.display = "flex";
      return;
    }
    event.target.nextElementSibling.style.display = "none";
    document.getElementById("settings").style.display = "none";
  },
  { passive: true }
);
