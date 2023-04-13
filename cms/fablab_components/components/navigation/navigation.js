const button = document.getElementById("menu-button");
const menu = document.getElementById("menu");
const search_form = document.getElementById("form-search");
const body = document.getElementById("body");

const bottom = document.getElementById("bottom");

const details = menu.getElementsByTagName("details");

button.addEventListener("click", (event) => {
  button.classList.toggle("close");
  bottom.classList.toggle("visible");
  body.classList.toggle("overflow");
});

document.addEventListener("click", (event) => {
  const target = event.target.parentNode;

  if (target.open) {
    target.setAttribute("open", "");
  }

  for (let detail of details) {
    if (detail !== target) {
      detail.removeAttribute("open");
    }
  }
});
