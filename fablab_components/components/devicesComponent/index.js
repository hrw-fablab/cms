const devicesSearch = document.getElementById("devices--search");
const devices = document.querySelectorAll(".device");

let searchConfig = {
  search: "",
  filter: "",
};

document
  .getElementById("print")
  .addEventListener("click", () => handleFilter("3D DRUCKER"));

document
  .getElementById("wood")
  .addEventListener("click", () => handleFilter("HOLZBEREICH"));

document
  .getElementById("metall")
  .addEventListener("click", () => handleFilter("METALL"));

const handleFilter = (filter) => {
  if (filter == searchConfig.filter) {
    searchConfig.filter = "";
    searchDevices();
    return;
  }
  searchConfig.filter = filter;
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
