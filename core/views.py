from django.http import JsonResponse
import json

import datetime

from calendar import monthrange

from organisation.models import Event


def get_more_tables(request):
    body = json.loads(request.body)
    events = []
    days = []
    date = datetime.date(body["year"], body["month"], 1)
    days_count = monthrange(body["year"], body["month"])[1]

    for element in Event.objects.all().order_by("start"):
        if element.visible(date) == True:
            events.append(element)

    for day in range(days_count):
        days.append([])
        for element in events:
            if element.day + 1 == day:
                days[day].append(
                    {
                        "title": element.title,
                        "adress": element.adress,
                        "length": element.length,
                        "timeStart": element.timeStart,
                        "timeEnd": element.timeEnd,
                    }
                )

    data = json.dumps(days)

    print(data)

    return JsonResponse(data, safe=False)
