from django.utils.translation import ugettext_lazy as _
from generic_chooser.widgets import AdminChooser
from site_models.models import Person

class PersonChooser(AdminChooser):
    choose_one_text = _("Choose a person")
    choose_another_text = _("Choose another person")
    link_to_chosen_text = _("Edit this person")
    model = Person
    choose_modal_url_name = "person_chooser:choose"
