from calendar import monthrange
import datetime
import json
from dateutil.relativedelta import relativedelta
from django_components import component
from events.models import Event
from django.db.models import Q

MONTHS = [
    "Januar",
    "Februar",
    "März",
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
    print(element)
    result = {
        "title": element.title,
        "adress": element.adress,
        "description": element.description,
        "category": element.category,
        "link": element.link,
        "link_text": element.link_text,
        "length": element.length,
        "start": element.timeStart,
        "end": element.timeEnd,
        "year": year,
        "month": month,
        "day": day,
        "monthString": MONTHS[int(month) - 1],
        "startDate": element.start.isoformat(),
        "endDate": element.end.isoformat(),
    }

    if element.repeatStart:
        result["repeatStart"] = int(element.repeatStart.strftime("%d"))
        result["startDate"] = datetime.datetime(
            year, month, day, element.start.hour, element.start.minute
        ).isoformat()
        result["endDate"] = datetime.datetime(
            year, month, day, element.end.hour, element.end.minute
        ).isoformat()

    if element.repeatEnd:
        result["repeatEnd"] = int(element.repeatEnd.strftime("%d"))

    if element.length >= 1:
        result["start"] = f"{day}. {MONTHS[element.month - 1]} {element.timeStart}"
        result[
            "end"
        ] = f"{day + element.length}. {MONTHS[element.month - 1]} {element.timeEnd}"

    return result


def get_repeats(element, year, month, day):
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


def get_events():
    result = []
    date = datetime.date.today()
    filter_elements = []

    max_iteration = 0

    while len(result) <= 4 and max_iteration <= 3:
        events = Event.objects.filter(
            (Q(start__gte=date) & Q(repeat="0") & ~Q(title__in=filter_elements))
            | (Q(repeat="1") & Q(repeatStart__lte=date) & Q(repeatEnd__gte=date))
        )

        for element in events:
            if element.repeat != "0":
                result.extend(get_repeats(element, date.year, date.month, date.day))
            else:
                filter_elements.append(element.title)
                result.append(get_event(element, date.year, element.month, element.day))

        date = date + relativedelta(months=1, day=1)
        max_iteration += 1

    result.sort(key=lambda x: x["day"])
    result.sort(key=lambda x: x["month"])

    return result[0:4]


@component.register("events")
class Events(component.Component):
    template_name = "events/index.html"

    def get_context_data(self):
        return {"events": get_events()}

    class Media:
        css = "events/index.css"
        js = "events/index.js"
