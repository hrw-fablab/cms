from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from organisation import models

from organisation.models.category import DeviceCategory

from generic_chooser.views import ModelChooserViewSet, ModelChooserMixin


class PersonChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['organisation','date']  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        organisation = self.request.GET.get('organisation')
        if organisation:
            objects = objects.filter(organisation_id=organisation)
        return objects


class PersonChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = models.Person
    page_title = _("Choose a person")
    per_page = 20
    order_by = "first_name"
    chooser_mixin_class = PersonChooserMixin


class ProjectChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = models.Project
    page_title = _("Choose a project")
    per_page = 10
    order_by = "name"


class DeviceCategoryChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = DeviceCategory
    page_title = _("Choose a device")
    per_page = 10
    order_by = "name"


class ProjectCategoryChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = models.ProjectCategory
    page_title = _("Choose a device")
    per_page = 10
    order_by = "name"

class OrganisationChooserViewSet(ModelChooserViewSet):
    icon = "group"
    model = models.Organisation
    page_title = _("Choose a organisation")
    per_page = 10
    order_by = "name"