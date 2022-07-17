const calendar = document.getElementById("calendar");
const date = document.getElementById("date");
const events = document.getElementById("events");

const backward = document.getElementById("backward");
const forward = document.getElementById("forward");
let elements = document.getElementsByTagName("details");

const months = [
  "Januar",
  "Februar",
  "Maerz",
  "April",
  "Mai",
  "Juni",
  "Juli",
  "August",
  "September",
  "Oktober",
  "November",
  "Dezember",
];

const categorys = ["none", "teach", "open", "student", "workshop", "external"];

let year = new Date().getFullYear();
let month_number = new Date().getMonth();
let month_string = months[month_number];

const handleChange = (event) => {
  if (event.target.id == "forward") {
    month_number += 1;
  } else {
    month_number -= 1;
  }

  if (month_number == 12) {
    year += 1;
    month_number = 0;
  }

  if (month_number == -1) {
    year -= 1;
    month_number = 11;
  }
  month_string = months[month_number];
  createCalendar();
};

const getCSRF = () => {
  let str = document.cookie;
  str = str.split("; ");
  const result = {};
  for (let i in str) {
    const cur = str[i].split("=");
    result[cur[0]] = cur[1];
  }
  return result.csrftoken;
};

const getData = async () => {
  const config = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRF(),
    },
    body: JSON.stringify({
      year: year,
      month: month_number + 1,
    }),
  };
  try {
    const data = await fetch("http://127.0.0.1:8000/events", config);
    const json = await data.json()
    return JSON.parse(json)
  } catch (error) {
    return [];
  }
};

const createEvent = (element, id) => {
  let details = document.createElement("details");
  details.dataset.type = categorys[element.category];

  if (id) {
    details.setAttribute("id", id);
    details.dataset.position = "first";
  }

  details.innerHTML = `
      <summary>
        <span class="date">${element.day} <br> ${months[month_number]}</span>
        ${element.timeStart} ${element.title}
      </summary>
      <div class="description">
        <header>
          <div>
            <h3>${element.title}</h3>
            <button class="close">
              <svg viewBox="0 0 24 24" width="24" height="24">
                <path d="m12 10.93 5.719-5.72c.146-.146.339-.219.531-.219.404 0 .75.324.75.749 0 .193-.073.385-.219.532l-5.72 5.719 5.719 5.719c.147.147.22.339.22.531 0 .427-.349.75-.75.75-.192 0-.385-.073-.531-.219l-5.719-5.719-5.719 5.719c-.146.146-.339.219-.531.219-.401 0-.75-.323-.75-.75 0-.192.073-.384.22-.531l5.719-5.719-5.72-5.719c-.146-.147-.219-.339-.219-.532 0-.425.346-.749.75-.749.192 0 .385.073.531.219z"/>
              </svg>
            </button>
          </div>
          <div>${element.timeStart} bis ${element.timeEnd}</div>
        </header>
        <p>${element.description}</p>
        <a href="${element.link || ""}">${element.link_text || ""}</>
      </div>
    `;

  return details;
};

const createFollower = (element, id, last) => {
  let button = document.createElement("button");
  button.innerHTML = `<span>${element.title}</span>`;
  button.value = id;
  button.dataset.type = categorys[element.category];

  if (last) {
    button.dataset.position = "last";
  } else {
    button.dataset.position = "middle";
  }
  return button;
};

document.addEventListener("click", () => {
  if (event.target.dataset.position) {
    let detail = document.getElementById(id);
    detail.toggleAttribute("open");
  }
});

const clearCalendar = () => {
  [...events.children].map((x) => {
    x.innerHTML = "";
    x.classList.remove("active");
  });
};

const createCalendar = async () => {
  clearCalendar();

  data = await getData();

  for (i = data.index; i < data.index + data.days; i++) {
    events.children[i].classList.add("active");
  }

  data.events.forEach((element) => {
    if (element.length == 1) {
      let li = document.getElementById(element.day + data.index);

      li.appendChild(createEvent(element));
      li.classList.add("full");
    }
  });

  data.events.forEach((element) => {
    if (element.length != 1) {
      for (i = 0; i < element.length + 1; i++) {
        let li = document.getElementById(element.day + i + data.index);
        id = "asdf";
        if (i == element.length) {
          li.appendChild(createFollower(element, id, true));
        } else if (i != 0) {
          li.appendChild(createFollower(element, id));
        } else {
          li.appendChild(createEvent(element, id));
          li.classList.add("full");
        }
      }
    }
  });

  updateDate();
};

const updateDate = () => {
  date.innerHTML = month_string + " " + year;
};

document.addEventListener("click", () => {
  if (event.target.className == "close") {
    event.target.parentNode.parentNode.parentNode.parentNode.toggleAttribute("open");
  }
});

window.addEventListener("load", createCalendar);

forward.addEventListener("click", handleChange);
backward.addEventListener("click", handleChange);
