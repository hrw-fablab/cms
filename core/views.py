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
    days = [[] for x in range(days_count)]

    for element in Event.objects.all().order_by("start"):
        if element.visible(date) == True:
            events.append(element)

    for element in events:
        if element.repeat == "0":
            days[element.day - 1].append(
                {
                    "title": element.title,
                    "adress": element.adress,
                    "length": element.length,
                    "timeStart": element.timeStart,
                    "timeEnd": element.timeEnd,
                    "day": element.day,
                    "description": element.description,
                }
            )
        else:
            for day in range(days_count):
                weekday = element.start.weekday()
                current_date = datetime.date(body["year"], body["month"], day + 1)
                if weekday == current_date.weekday():
                    days[day].append(
                        {
                            "title": element.title,
                            "adress": element.adress,
                            "length": element.length,
                            "timeStart": element.timeStart,
                            "timeEnd": element.timeEnd,
                            "day": day,
                            "description": element.description,
                        }
                    )

    data = json.dumps(days)

    return JsonResponse(data, safe=False)
