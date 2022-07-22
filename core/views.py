from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from organisation.models import Event

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
        days.append(
            {
                "title": element.title,
                "adress": element.adress,
                "link": element.link,
                "link_text": element.link_text,
                "length": element.length,
                "timeStart": element.timeStart,
                "timeEnd": element.timeEnd,
                "day": element.day,
                "month": body["month"],
                "year": body["year"],
                "start": element.start.weekday(),
                "repeat": element.repeat,
                "description": element.description,
                "category": element.category,
                "expections": expections,
            }
        )
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
