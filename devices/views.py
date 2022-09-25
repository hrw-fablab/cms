from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from core.models import FablabImage

from .models import Device

from .utils import load_data


def index(request):
    return render(request, "devices/index.html")


def load(request):
    Device.objects.all().delete()
    devices = []
    data = load_data()
    for item in data:
        if item["image"] == False:
            image = None
        else:
            image = FablabImage.objects.filter(title=item["image"]).first()
        devices.append(
            Device(
                title=item["title"],
                model=item["model"],
                area=item["area"],
                manufacturer=item["manufacturer"],
                image=image,
            )
        )
    Device.objects.bulk_create(devices)
    return HttpResponseRedirect(reverse("devices_admin:index"))
