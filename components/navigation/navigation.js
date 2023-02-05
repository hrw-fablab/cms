const navigation = document.getElementById("navigation");

document.addEventListener("scroll", () => {
  if (document.documentElement.scrollTop > 600) {
    navigation.classList.add("blur");
  } else {
    navigation.classList.remove("blur");
  }
});
