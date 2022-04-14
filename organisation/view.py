from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from organisation.models import Person, Project
from organisation.models.category import DeviceCategory


class PersonChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = Person
    page_title = _("Choose a person")
    per_page = 20
    order_by = "first_name"
    fields = ["first_name", "last_name"]


class ProjectChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = Project
    page_title = _("Choose a project")
    per_page = 10
    order_by = "name"
    fields = ["name"]


class DeviceCategoryChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = DeviceCategory
    page_title = _("Choose a device")
    per_page = 10
    order_by = "name"
    fields = ["name"]
