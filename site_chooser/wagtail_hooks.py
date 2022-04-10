from wagtail.core import hooks
from .views import PersonChooserViewSet

from django.utils.translation import gettext_lazy as _


@hooks.register("register_admin_viewset")
def register_person_chooser_viewset():
    return PersonChooserViewSet("person_chooser", url_prefix="person-chooser")