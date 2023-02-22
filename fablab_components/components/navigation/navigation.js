const button = document.getElementById("menu-button");
const menu = document.getElementById("menu");
const search_form = document.getElementById("form-search");
const body = document.getElementById("body");

const bottom = document.getElementById("bottom");

button.addEventListener("click", (event) => {
  button.classList.toggle("close");
  bottom.classList.toggle("visible");
  body.classList.toggle("overflow");
});
