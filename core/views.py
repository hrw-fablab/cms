from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from organisation.models import Event


def get_events(request):
    body = json.loads(request.body)
    events = []
    days = []
    date = datetime.date(body["year"], body["month"], 1)
    days_count = monthrange(body["year"], body["month"])[1]

    for element in Event.objects.all().order_by("start"):
        if element.visible(date) == True:
            events.append(element)

    print(events)

    for day in range(days_count):
        days.append([])
        for element in events:
            if element.repeat == 1:
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
                            "description": element.description,
                        }
                    )
            if element.day + 1 == day and element.repeat != 1:
                days[day].append(
                    {
                        "title": element.title,
                        "adress": element.adress,
                        "length": element.length,
                        "timeStart": element.timeStart,
                        "timeEnd": element.timeEnd,
                        "description": element.description,
                    }
                )

    data = json.dumps(days)

    return JsonResponse(data, safe=False)
