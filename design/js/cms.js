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
      document.getElementById("form-search").style.display = "flex";
      return;
    }
    event.target.nextElementSibling.style.display = "none";
    document.getElementById("form-search").style.display = "none";
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

function debounce(func, delay = 250) {
  let timerId;
  return (...args) => {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}
const search = document.getElementById("search");
const results = document.getElementById("results");

const input = async (event) => {
  resetResults();
  if (event.target.value.length <= 1) {
    results.style.display = "none";
    return;
  }
  const query = event.target.value;
  const res = await fetch(
    `${window.location.origin}/search_json/?${new URLSearchParams({
      query,
    }).toString()}`
  );
  const data = await res.json();
  if (data.length != 0) {
    displayResults(data);
  } else {
    results.style.display = "none";
  }
};

const displayResults = (data) => {
  results.style.display = "flex";
  data.map((item) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <a href=${item.url}>${item.title}</a>
      `;
    results.appendChild(li);
  });
};

const resetResults = () => {
  results.innerHTML = "";
};

search.addEventListener("input", debounce(input));
