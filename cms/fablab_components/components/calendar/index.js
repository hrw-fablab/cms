document.getElementById("calendar").addEventListener("click", () => {
  const details = document
    .getElementById("calendar")
    .getElementsByTagName("details");

    for (item of details) {
        item.open = false;
    }
});
