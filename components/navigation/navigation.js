const navigation = document.getElementById("navigation");
const button = document.getElementById("menu-button");
const menu = document.getElementById("menu");

document.addEventListener("DOMContentLoaded", () => {
  if (document.documentElement.scrollTop > 100) {
    navigation.classList.add("shadow");
  } else {
    navigation.classList.remove("shadow");
  }
});

document.addEventListener("scroll", () => {
  if (document.documentElement.scrollTop > 100) {
    navigation.classList.add("shadow");
  } else {
    navigation.classList.remove("shadow");
  }
});

button.addEventListener("click", (event) => {
  console.log("yes");
  menu.classList.toggle("visible");
  document.getElementById("form-search").classList.toggle("visible");
});
