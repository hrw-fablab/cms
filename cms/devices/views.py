from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from cms.core.models import FablabImage

from .models import Device

from .utils import enhance_data, load_data, load_images, reduce_data, create_devices


def index(request):
    return render(request, "devices/index.html", {"devices": Device.objects.all()})


def load(request):
    Device.objects.all().delete()
    devices = []

    data = load_data()

    enhanced = enhance_data(data)
    reduced = reduce_data(enhanced)

    load_images(reduced)

    devices = create_devices(reduced)

    Device.objects.bulk_create(devices)
    return HttpResponseRedirect(reverse("devices_admin:index"))


def delete(request):
    Device.objects.all().delete()

    FablabImage.objects.all().filter(collection__name="devices").delete()

    return HttpResponseRedirect(reverse("devices_admin:index"))
