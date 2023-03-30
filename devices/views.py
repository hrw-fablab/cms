from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from core.models import FablabImage

from .models import Device

from .utils import enhance_data, filter_data, load_data, load_images, reduce_data


def index(request):
    return render(request, "devices/index.html")


def link_image(item):
    if not item:
        return None
    return FablabImage.objects.filter(title=item).first()


def create_devices(data):
    devices = []
    for item in data:
        devices.append(
            Device(
                title=item["title"],
                model=item["model"],
                area=item["area"],
                manufacturer=item["manufacturer"],
                amount=item["amount"],
                image=link_image(item["image"]),
            )
        )
    return devices


def load(request):
    Device.objects.all().delete()
    devices = []

    data = load_data()
    enhanced = enhance_data(data)
    reduced = reduce_data(enhanced)

    images = load_images(reduced)

    devices = create_devices(reduced)

    Device.objects.bulk_create(devices)
    return HttpResponseRedirect(reverse("devices_admin:index"))
