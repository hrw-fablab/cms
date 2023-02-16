const button = document.getElementById("menu-button");
const menu = document.getElementById("menu");
const body = document.getElementById("body");

button.addEventListener("click", (event) => {
  menu.classList.toggle("visible");
  body.classList.toggle("overflow");
});
