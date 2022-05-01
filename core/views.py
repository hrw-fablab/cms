from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

import datetime

from django.core import serializers

from organisation.models import Event


def get_more_tables(request):
    body = json.loads(request.body)
    events = []

    date = datetime.date(body["year"], body["month"], 1)

    for element in Event.objects.all():
        if element.visible(date) == True:
            events.append(element)

    data = serializers.serialize("json", events)

    return JsonResponse(data, safe=False)
