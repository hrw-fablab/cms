const navigation = document.getElementById("navigation");
const button = document.getElementById("menu-button");
const menu = document.getElementById("menu");

document.addEventListener("DOMContentLoaded", () => {
  if (document.documentElement.scrollTop > 600) {
    navigation.classList.add("blur");
  } else {
    navigation.classList.remove("blur");
  }
});

document.addEventListener("scroll", () => {
  if (document.documentElement.scrollTop > 600) {
    navigation.classList.add("blur");
  } else {
    navigation.classList.remove("blur");
  }
});

button.addEventListener("click", (event) => {
  console.log("yes");
  menu.classList.toggle("visible");
  document.getElementById("form-search").classList.toggle("visible");
});
