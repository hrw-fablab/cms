from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Device

from .utils import load_data


def index(request):
    return render(request, "devices/index.html")


def load(request):
    Device.objects.all().delete()
    devices = []
    data = load_data()
    for item in data:
        devices.append(
            Device(
                title=item["title"],
                model=item["model"],
                area=item["area"],
                manufacturer=item["manufacturer"],
            )
        )
    Device.objects.bulk_create(devices)
    return HttpResponseRedirect(reverse("devices_admin:index"))
