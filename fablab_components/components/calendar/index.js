const calendar = document.getElementById("calendar");
const date = document.getElementById("date");
const events = document.getElementById("days");

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

let year = new Date().getFullYear();
let month_number = new Date().getMonth();
let month_string = months[month_number];

const handleChange = (event) => {
  console.log(event.target.id);
  if (event.target.id == "forward") {
    month_number += 1;
  } else {
    month_number -= 1;
  }

  console.log(month_number);

  if (month_number == 12) {
    year += 1;
    month_number = 0;
  }

  if (month_number == -1) {
    year -= 1;
    month_number = 11;
  }
  month_string = months[month_number];
  console.log(month_string);
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

const getData = async (url) => {
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
    const data = await fetch(`${window.location.origin}/calendar`, config);
    const json = await data.json();
    return JSON.parse(json);
  } catch (error) {
    return { events: [] };
  }
};

const createEvent = (element, id, category, position, day) => {
  let div = document.createElement("div");

  let desktop = document.createElement("details");
  let mobile = document.createElement("div");

  div.dataset.type = category;
  div.dataset.position = position;

  let start = element.timeStart;
  let end = element.timeEnd;

  if (element.length >= 1) {
    start = `${day}. ${months[element.month - 1]} ${element.timeStart}`;
    end = `${day + element.length}. ${months[element.month - 1]} ${
      element.timeEnd
    }`;
  }

  desktop.setAttribute("class", "desktop");
  desktop.setAttribute("id", id);
  mobile.setAttribute("class", "mobile");

  desktop.innerHTML = `
      <summary>
        <span class="title"> ${element.title}</span>
      </summary>
      <div class="description">
        <header>
          <div>
            <h3>${element.title}</h3>
            <button class="close" data-close="">
              <svg viewBox="0 0 24 24" width="24" height="24">
                <path d="m12 10.93 5.719-5.72c.146-.146.339-.219.531-.219.404 0 .75.324.75.749 0 .193-.073.385-.219.532l-5.72 5.719 5.719 5.719c.147.147.22.339.22.531 0 .427-.349.75-.75.75-.192 0-.385-.073-.531-.219l-5.719-5.719-5.719 5.719c-.146.146-.339.219-.531.219-.401 0-.75-.323-.75-.75 0-.192.073-.384.22-.531l5.719-5.719-5.72-5.719c-.146-.147-.219-.339-.219-.532 0-.425.346-.749.75-.749.192 0 .385.073.531.219z"/>
              </svg>
            </button>
          </div>
          <div>${start} - ${end}</div>
        </header>
        <p>${element.description}</p>
        ${
          element.link
            ? `<a href="${element.link}">${element.link_text}</a>`
            : ""
        }
      </div>
    `;

  mobile.innerHTML = `
    <section>
        <time>${day}. ${month_string}</time>
        <div>
            <header>
            ${
              element.link
                ? `<a href="${element.link}"><h3>${element.title}</h3></a>`
                : `<h3>${element.title}</h3>`
            }
                <time>${start} bis ${end}</time>
            </header>
            <p>${element.description}</p>
        </div>
    </section>
    `;

  div.appendChild(desktop);
  div.appendChild(mobile);
  return div;
};

const createRedirect = (id, category, position) => {
  let button = document.createElement("button");
  button.innerHTML = `<span>.</span>`;
  button.value = id;
  button.dataset.position = position;
  button.dataset.redirect = "";
  button.dataset.type = category;

  return button;
};

document.addEventListener("click", (event) => {
  if ("redirect" in event.target.dataset) {
    document.getElementById(event.target.value).toggleAttribute("open");
  }

  if ("close" in event.target.dataset) {
    event.target.parentNode.parentNode.parentNode.parentNode.toggleAttribute(
      "open"
    );
  }
});

const clearCalendar = () => {
  [...events.children].map((x) => {
    x.innerHTML = "";
    x.classList.remove("active");
    x.classList.remove("full");
  });
};

const addEvent = (li, element, id, category, position, day) => {
  li.classList.add("full");
  li.appendChild(createEvent(element, id, category, position, day));
};

const addRedirect = (li, id, category, position) => {
  li.appendChild(createRedirect(id, category, position));
};

const checkExpection = (expections, check) => {
  let result = false;
  expections.map((expection) => {
    let start = new Date(
      expection.start.year,
      expection.start.month - 1,
      expection.start.day
    );
    let end = new Date(
      expection.end.year,
      expection.end.month - 1,
      expection.end.day
    );

    if (check >= start && check <= end) {
      result = true;
    }
  });

  return result;
};

const createCalendar = async () => {
  clearCalendar();

  const data = await getData(`${window.location.hostname}/calendar`);

  for (let i = data.index; i < data.index + data.days; i++) {
    events.children[i].classList.add("active");
  }

  data.events.forEach((element, i) => {
    let li = document.getElementById(element.day + data.index);
    let id = `event${i}`;
    if (element.repeat) {
      element.repeat.map((item) =>
        addEvent(
          events.children[item + data.index],
          element,
          id,
          element.category,
          undefined,
          item + 1
        )
      );
      return;
    }

    if (element.length >= 1) {
      addEvent(li, element, id, element.category, "first", element.day);
      for (i = 0; i < element.length; i++) {
        let redirect = document.getElementById(
          element.day + i + data.index + 1
        );
        if (i == element.length - 1) {
          addRedirect(redirect, id, element.category, "last");
          return;
        }
        addRedirect(redirect, id, element.category);
      }

      return;
    }

    addEvent(li, element, id, element.category, undefined, element.day);
  });

  updateDate();
};

const updateDate = () => {
  date.innerHTML = month_string + " " + year;
};

window.addEventListener("load", createCalendar);

forward.addEventListener("click", handleChange);
backward.addEventListener("click", handleChange);
