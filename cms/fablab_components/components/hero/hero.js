const video = document.getElementById("hero-video");
const control = document.getElementById("control");
const play = document.getElementById("play");
const pause = document.getElementById("pause");

document.getElementById("control").addEventListener("click", () => {
  play.classList.remove("visible");
  if (video.paused) {
    play.classList.add("hidden");
    pause.classList.remove("hidden");
    video.play();
    return;
  }

  play.classList.remove("hidden");
  pause.classList.add("hidden");
  video.pause();
});
