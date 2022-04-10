from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from .models import Person

class PersonChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = Person
    page_title = _("Choose a person")
    per_page = 10
    order_by = "name"
    fields = ["name"]
