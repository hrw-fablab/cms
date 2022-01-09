document.addEventListener("click", (event)=> {
	if (event.target.tagName == "BUTTON") {
		if (getComputedStyle(event.target.nextElementSibling).display === "none") {
			for (element of document.getElementsByClassName("submenu")) { element.classList.add("hidden") }
			return event.target.nextElementSibling.classList.remove("hidden")
		}
		return event.target.nextElementSibling.classList.add("hidden")
	}
	for (element of document.getElementsByClassName("submenu")) { element.classList.add("hidden") }
});