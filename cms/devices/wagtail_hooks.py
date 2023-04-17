from django.urls import include, path, reverse
from django.utils.translation import gettext_lazy as _
from wagtail.admin.menu import MenuItem
from wagtail import hooks

from cms.devices import urls


class DeviceMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path("devices/", include((urls, "devices"), namespace="devices_admin")),
    ]


@hooks.register("register_settings_menu_item")
def register_devices_menu():
    return DeviceMenuItem(
        _("Geräte"), reverse("devices_admin:index"), icon_name="list-ul"
    )
