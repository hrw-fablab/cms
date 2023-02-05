// Function to handle Display of Menu on Mobile Navigation

document.addEventListener("mousemove", (event) => {
  if (event.target.nodeName !== "A") return;
  const rect = event.target.getBoundingClientRect();
  let x = event.clientX - rect.left;
  let y = event.clientY - rect.top + rect.height;
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
