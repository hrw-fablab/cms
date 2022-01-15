document.addEventListener("click", (event) => {
	if (event.target.tagName == "BUTTON" && event.target.id != "menu-button") {
		console.log("1");
		if (getComputedStyle(event.target.nextElementSibling).display === "none") {
			console.log("2");
			for (element of document.getElementsByClassName("submenu")) { element.classList.add("hidden") }
			return event.target.nextElementSibling.classList.remove("hidden")
		}
		return event.target.nextElementSibling.classList.add("hidden")
	}
	for (element of document.getElementsByClassName("submenu")) { element.classList.add("hidden") }
});

document.getElementById("menu-button").addEventListener("click", (event) => {
	if (getComputedStyle(event.target.nextElementSibling).display === "none") {
		event.target.nextElementSibling.style.display = "flex";
		return;
	}
	event.target.nextElementSibling.style.display = "none";
})