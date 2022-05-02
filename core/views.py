from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

import datetime

from calendar import calendar, monthrange, month_name

from django.core import serializers

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
                days[day].append({"title": element.title})

    data = json.dumps(days)

    return JsonResponse(data, safe=False)
