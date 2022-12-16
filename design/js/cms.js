// Function to handle Display of Menu on Mobile Navigation
document.getElementById("menu-button").addEventListener(
  "click",
  (event) => {
    event.target.nextElementSibling.classList.toggle("visible");
    document.getElementById("form-search").classList.toggle("visible");
  },
  { passive: true }
);

document.addEventListener("mousemove", (event) => {
  if (!event.target.classList.contains("card")) return;
  const rect = event.target.getBoundingClientRect();
  let x = event.clientX - rect.left;
  let y = event.clientY - rect.top;
  event.target.style.setProperty("--mouse-x", `${x}px`);
  event.target.style.setProperty("--mouse-y", `${y}px`);
});

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
  if (event.target.value.length <= 2) {
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
