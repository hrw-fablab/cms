from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser

from .models import Person, Project

class PersonChooser(AdminChooser):
    choose_one_text = _("Choose a person")
    choose_another_text = _("Choose another person")
    link_to_chosen_text = _("Edit this person")
    model = Person
    choose_modal_url_name = "person_chooser:choose"


class ProjectChooser(AdminChooser):
    choose_one_text = _("Choose a Project")
    choose_another_text = _("Choose another Project")
    link_to_chosen_text = _("Edit this Project")
    model = Project
    choose_modal_url_name = "project_chooser:choose"