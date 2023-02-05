const search = document.getElementById("search");
const results = document.getElementById("results");

const debounce = (func, delay = 250) => {
  let timerId;
  return (...args) => {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
};

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
