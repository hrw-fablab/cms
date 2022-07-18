from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from organisation.models import Event


def single_append(element, year, month):
    return {
        "title": element.title,
        "adress": element.adress,
        "link": element.link,
        "link_text": element.link_text,
        "length": element.length,
        "timeStart": element.timeStart,
        "timeEnd": element.timeEnd,
        "day": element.day,
        "month": month,
        "year": year,
        "description": element.description,
        "category": element.category,
    }


def repeat_append(element, count, year, month):
    results = []
    for day in range(count):
        switch = True
        weekday = element.start.weekday()
        current_date = datetime.date(year, month, day + 1)

        for exception in element.related_expection.all():
            if (current_date >= exception.start and current_date <= exception.end):
                switch = False

        if weekday == current_date.weekday() and switch == True:
            results.append(
                {
                    "title": element.title,
                    "adress": element.adress,
                    "link": element.link,
                    "link_text": element.link_text,
                    "length": element.length,
                    "timeStart": element.timeStart,
                    "timeEnd": element.timeEnd,
                    "day": day + 1,
                    "month": month,
                    "year": year,
                    "description": element.description,
                    "category": element.category,
                    "repeat": 1,
                }
            )
    return results


def repeat_append_filter(element, count, year, month):
    results = []
    for day in range(count):
        switch = True
        weekday = element.start.weekday()
        current_date = datetime.date(year, month, day + 1)

        for exception in element.related_expection.all():
            if (current_date >= exception.start and current_date <= exception.end):
                switch = False

        if weekday == current_date.weekday() and day <= element.repeatEnd.day and switch == True:
            results.append(
                {
                    "title": element.title,
                    "adress": element.adress,
                    "link": element.link,
                    "link_text": element.link_text,
                    "length": element.length,
                    "timeStart": element.timeStart,
                    "timeEnd": element.timeEnd,
                    "day": day + 1,
                    "month": month,
                    "year": year,
                    "description": element.description,
                    "category": element.category,
                    "repeat": 1,
                }
            )
    return results


def get_events(request):
    body = json.loads(request.body)
    events = []
    date = datetime.date(body["year"], body["month"], 1)
    days_count = monthrange(body["year"], body["month"])[1]
    days = []

    for element in Event.objects.all().order_by("start"):
        if element.visible(date) == True:
            events.append(element)

    for element in events:
        if element.repeat == "0":
            days.append(single_append(element, date.year, date.month))
        elif (
            element.repeatEnd.month == date.month
            and element.repeatEnd.year == date.year
        ):
            days.extend(
                repeat_append_filter(element, days_count, date.year, date.month)
            )
        else:
            days.extend(repeat_append(element, days_count, date.year, date.month))

    days.sort(key = lambda x: x['length'])

    result = {
        "year": body["year"],
        "month": body["month"],
        "days": days_count,
        "index": date.weekday(),
        "events": days
    }

    data = json.dumps(result)

    return JsonResponse(data, safe=False)
