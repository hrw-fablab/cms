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

    print(events)

    for element in events:
        if element.repeat == "0":
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
                    "description": element.description,
                    "category": element.category,
                }
            )
        else:
            for day in range(days_count):
                weekday = element.start.weekday()
                current_date = datetime.date(body["year"], body["month"], day + 1)
                if weekday == current_date.weekday():
                    days.append(
                        {
                            "title": element.title,
                            "adress": element.adress,
                            "link": element.link,
                            "link_text": element.link_text,
                            "length": element.length,
                            "timeStart": element.timeStart,
                            "timeEnd": element.timeEnd,
                            "day": day + 1,
                            "description": element.description,
                            "category": element.category,
                            "repeat": 1,
                        }
                    )

    data = json.dumps(days)

    return JsonResponse(data, safe=False)
