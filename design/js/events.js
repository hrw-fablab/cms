const calendar = document.getElementById("calendar");
const events = document.getElementById("events");

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

const getData = async (url, year, month) => {
  const config = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRF(),
    },
    body: JSON.stringify({
      year: year,
      month: month,
    }),
  };
  try {
    const data = await fetch(url, config);
    const json = await data.json();
    return JSON.parse(json);
  } catch (error) {
    return [];
  }
};

const createEvent = (element, category) => {
  let section = document.createElement("section");

  section.innerHTML = `
      <time data-type="${category}">${element.day} ${months[element.month - 1]}</time>
      <header>
      <a href="${element.link}"><h3>${element.title}</h3></a>
      <time>${element.timeStart} bis ${element.timeEnd}</time>
      </header>
      <div>
        <p>${element.description}</p>
      </div>
    `;

  return section;
};

const createCalendar = async () => {
  let month = 1;
  let date = new Date();
  while (events.children.length <= 3) {
    const data = await getData(
      `${window.location.origin}/events`,
      date.getFullYear(),
      date.getMonth() + month
    );

    for (const element of data.events) {
      if (
        element.day <= date.getDate() &&
        element.month == new Date().getMonth() + 1
      ) {
        break;
      }
      if (events.children.length >= 3) {
        break;
      }
      events.appendChild(createEvent(element, categorys[element.category]))
    }
    month++;
  }
};

window.addEventListener("load", createCalendar);
