// Function to handle Display of Menu on Mobile Navigation

document.addEventListener("mousemove", (event) => {
  if (event.target.nodeName !== "A") return;
  const rect = event.target.getBoundingClientRect();
  let x = event.clientX - rect.left;
  let y = event.clientY - rect.top + rect.height;
  event.target.style.setProperty("--mouse-x", `${x}px`);
  event.target.style.setProperty("--mouse-y", `${y}px`);
});
