from django import template

register = template.Library()

import datetime
from calendar import monthrange
from events.models import Event
from dateutil.relativedelta import relativedelta

MONTHS = [
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
]


def get_event(element, year, month, day):
    result = {
        "title": element.title,
        "adress": element.adress,
        "link": element.link,
        "link_text": element.link_text,
        "length": element.length,
        "start": element.timeStart,
        "end": element.timeEnd,
        "day": day,
        "month": MONTHS[int(month) - 1],
        "year": year,
        "description": element.description,
        "category": element.category,
    }

    if element.length >= 1:
        result["start"] = f"{day}. {MONTHS[element.month - 1]} {element.timeStart}"
        result[
            "end"
        ] = f"{day + element.length}. {MONTHS[element.month - 1]} {element.timeEnd}"

    if element.repeatStart:
        result["repeatStart"] = int(element.repeatStart.strftime("%d"))

    if element.repeatEnd:
        result["repeatEnd"] = int(element.repeatEnd.strftime("%d"))

    return result


def get_repeated_event(element, year, month, day):
    repeated = []
    count = monthrange(year, month)[1]
    weekday = element.start.weekday()

    for days in range(count):
        switch = True
        current_date = datetime.date(year, month, days + 1)

        for exception in element.related_expection.all():
            if current_date >= exception.start and current_date <= exception.end:
                switch = False

        if weekday == current_date.weekday() and switch and current_date.day >= day:
            repeated.append(get_event(element, year, month, current_date.day))

    return repeated


@register.simple_tag
def get_events():
    date = datetime.date.today()
    events = []

    switch = False
    iteration = 0

    while switch == False:
        for element in Event.objects.all():
            if element.visible_events(date):
                if element.repeat != "0":
                    events.extend(
                        get_repeated_event(element, date.year, date.month, date.day)
                    )
                else:
                    events.append(
                        get_event(element, date.year, element.month, element.day)
                    )
        if len(events) >= 5 or iteration >= 5:
            switch = True
        iteration = iteration + 1
        date = datetime.date(date.year, date.month, 1) + relativedelta(months=+1)

    events.sort(key=lambda x: x["day"])
    events.sort(key=lambda x: x["month"], reverse=True)

    return events[0:3]
