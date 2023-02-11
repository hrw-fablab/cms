const devicesSearch = document.getElementById("devices--search");
const devices = document.querySelectorAll(".device");
const filterButtons = document.querySelectorAll(".filter--button");

let searchConfig = {
  search: "",
  filter: "",
};

document
  .getElementById("print")
  .addEventListener("click", (event) => handleFilter(event, "3D DRUCKER"));

document
  .getElementById("wood")
  .addEventListener("click", (event) => handleFilter(event, "HOLZBEREICH"));

document
  .getElementById("metall")
  .addEventListener("click", (event) => handleFilter(event, "METALL"));

const handleFilter = (event, filter) => {
  filterButtons.forEach((element) => element.classList.remove("active"));
  if (filter == searchConfig.filter) {
    searchConfig.filter = "";
    event.target.classList.remove("active");
    searchDevices();
    return;
  }
  searchConfig.filter = filter;
  event.target.classList.add("active");
  searchDevices();
};

const searchDevices = () => {
  devices.forEach((device) => {
    if (!device.dataset.title || !device.dataset.area) return;

    if (
      searchConfig.filter != device.dataset.area &&
      searchConfig.filter.length != 0
    ) {
      device.style.display = "none";
      return;
    }

    if (device.dataset?.title.indexOf(searchConfig.search) == -1) {
      device.style.display = "none";
      return;
    }

    device.style.display = "";
  });
};

devicesSearch.addEventListener("input", (event) => {
  searchConfig.search = event.target.value.toUpperCase();

  searchDevices();
});
