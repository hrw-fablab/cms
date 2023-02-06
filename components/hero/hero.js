const video = document.getElementById("hero-video");
const control = document.getElementById("control");
const play = document.getElementById("play");
const pause = document.getElementById("pause");

window.onload = addAutoplay();

function addAutoplay() {
  control.style.opacity = 1;
  if (window.innerWidth > 992) {
    control.style.opacity = "";
    pause.style.display = "block";
    play.style.display = "none";
    video.setAttribute("autoplay", "");
  }
}

document.getElementById("control").addEventListener("click", () => {
  control.style.opacity = "";
  if (video.paused) {
    pause.style.display = "block";
    play.style.display = "none";
    video.play();
    return;
  }

  pause.style.display = "none";
  play.style.display = "block";
  video.pause();
});
