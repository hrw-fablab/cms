const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add("show");
  });
});

//const embed = document.querySelectorAll(".hidden");
//embed.forEach((el) => observer.observe(el));
