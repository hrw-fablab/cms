from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from cms.events.models import Event

from dotenv import load_dotenv

load_dotenv()


def get_repeated_event_days(element, year, month, day):
    repeated = []
    count = monthrange(year, month)[1]
    weekday = element.start.weekday()

    if element.repeatStart.month == month:
        for days in range(count):
            switch = True
            current_date = datetime.date(year, month, days + 1)

            for exception in element.related_expection.all():
                if current_date >= exception.start and current_date <= exception.end:
                    switch = False

            if (
                weekday == current_date.weekday()
                and switch
                and current_date.day > element.repeatStart.day
            ):
                repeated.append(days)

        return repeated

    for days in range(count):
        switch = True
        current_date = datetime.date(year, month, days + 1)

        for exception in element.related_expection.all():
            if current_date >= exception.start and current_date <= exception.end:
                switch = False

        if weekday == current_date.weekday() and switch:
            repeated.append(days)

    return repeated


def get_event(element, year, month, day):
    result = {
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
        "description": element.description,
        "category": element.category,
    }

    if element.repeat != "0":
        result["repeat"] = get_repeated_event_days(element, year, month, day)

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


def get_calendar(request):
    body = json.loads(request.body)
    date = datetime.date(body["year"], body["month"], 1)
    days_count = monthrange(body["year"], body["month"])[1]
    days = []

    for element in Event.objects.all().order_by("start"):
        if element.visible_calendar(date):
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
