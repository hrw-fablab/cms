from cms.core.models import FablabBasePage

from cms.devices.models import Device


class DeviceIndexPage(FablabBasePage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = [""]

    template = "pages/devices.html"

    def get_context(self, request):
        context = super().get_context(request)
        devices = Device.objects.all().order_by("-area")
        context["devices"] = devices
        return context

    class Meta:
        verbose_name = "Geräte"
