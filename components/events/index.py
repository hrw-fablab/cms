from calendar import monthrange
import datetime
from django_components import component
from organisation.models import Event
from django.db.models import Q

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

    events = Event.objects.filter(
        (
            Q(start__year=str(date.year))
            & Q(start__month=str(date.month))
            & Q(repeat="0")
        )
        | (Q(repeat="1") & Q(repeatStart__lte=date) & Q(repeatEnd__gte=date))
    )

    for element in events:
        if element.repeat != "0":
            result.extend(get_repeats(element, date.year, date.month, date.day))
        else:
            result.append(get_event(element, date.year, element.month, element.day))

    result.sort(key=lambda x: x["day"])
    result.sort(key=lambda x: x["month"], reverse=True)

    return result[0:4]


@component.register("events")
class Events(component.Component):
    template_name = "events/index.html"

    def get_context_data(self):
        return {"events": get_events()}

    class Media:
        css = "events/index.css"
        js = "events/index.js"
