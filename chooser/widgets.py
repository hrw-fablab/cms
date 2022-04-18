from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from organisation import models

from organisation.models.category import DeviceCategory
from organisation.models.organisation import Organisation



class PersonChooser(LinkedFieldMixin, AdminChooser):
    choose_one_text = _("Choose a person")
    choose_another_text = _("Choose another person")
    link_to_chosen_text = _("Edit this person")
    model = models.Person
    choose_modal_url_name = "person_chooser:choose"


class ProjectChooser(AdminChooser):
    choose_one_text = _("Choose a Project")
    choose_another_text = _("Choose another Project")
    link_to_chosen_text = _("Edit this Project")
    model = models.Project
    choose_modal_url_name = "project_chooser:choose"


class DeviceCategoryChooser(AdminChooser):
    choose_one_text = _("Choose a Device Category")
    choose_another_text = _("Choose another Device Category")
    link_to_chosen_text = _("Edit this Device Category")
    model = DeviceCategory
    choose_modal_url_name = "devicecategory_chooser:choose"

class OrganisationChooser(AdminChooser):
    choose_one_text = _("Choose a Organisation")
    choose_another_text = _("Choose another Organisation")
    link_to_chosen_text = _("Edit this Organisation")
    model = Organisation
    choose_modal_url_name = "organisation_chooser:choose"