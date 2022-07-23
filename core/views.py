from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from organisation.models import Event


def get_expections(element):
    expections = []
    for expection in element.related_expection.all():
        expections.append(
            {
                "start": {
                    "year": expection.start.strftime("%Y"),
                    "month": expection.start.strftime("%m"),
                    "day": expection.start.strftime("%d"),
                },
                "end": {
                    "year": expection.end.strftime("%Y"),
                    "month": expection.end.strftime("%m"),
                    "day": expection.end.strftime("%d"),
                },
            }
        )

    return expections


def get_event(element, year, month, day):
    return {
        "title": element.title,
        "adress": element.adress,
        "link": element.link,
        "link_text": element.link_text,
        "length": element.length,
        "timeStart": element.timeStart,
        "timeEnd": element.timeEnd,
        "day": day,
        "month": month,
        "year": year,
        "start": element.start.weekday(),
        "repeat": element.repeat,
        "description": element.description,
        "category": element.category,
        "expections": get_expections(element),
    }


def get_repeated_event(element, year, month, day):
    repeated = []
    count = monthrange(year, month)[1]

    for days in range(count):
        switch = True
        weekday = element.start.weekday()
        current_date = datetime.date(year, month, days + 1)

        for exception in element.related_expection.all():
            if current_date >= exception.start and current_date <= exception.end:
                switch = False

        if weekday == current_date.weekday() and switch and current_date.day > day:
            repeated.append(get_event(element, year, month, current_date.day))

    return repeated


def get_events(request):
    body = json.loads(request.body)
    date = datetime.date(body["year"], body["month"], body["day"])

    events = []

    while len(events) < 3:
        for element in Event.objects.all().order_by("start"):
            if (
                element.visible_year(date)
                and element.visible_month(date)
                and element.visible_day(date)
            ):
                if element.repeat != "0":
                    events.extend(
                        get_repeated_event(element, date.year, date.month, date.day)
                    )
                else:
                    events.append(
                        get_event(element, date.year, date.month, element.day)
                    )
            if len(events) < 3:
                date = datetime.date(body["year"], body["month"] + 1, 1)
                break

    result = {"events": events[0:3]}

    data = json.dumps(result)
    return JsonResponse(data, safe=False)


def get_calendar(request):
    body = json.loads(request.body)
    date = datetime.date(body["year"], body["month"], 1)
    days_count = monthrange(body["year"], body["month"])[1]
    days = []

    for element in Event.objects.all().order_by("start"):
        if element.visible_year(date) and element.visible_month(date):
            days.append(get_event(element, body["year"], body["month"], element.day))

    days.sort(key=lambda x: x["length"])

    result = {
        "year": body["year"],
        "month": body["month"],
        "days": days_count,
        "index": date.weekday(),
        "events": days,
    }
    data = json.dumps(result)
    return JsonResponse(data, safe=False)
