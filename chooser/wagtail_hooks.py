from wagtail.core import hooks

from .view import PersonChooserViewSet


@hooks.register("register_admin_viewset")
def register_person_chooser_viewset():
    return PersonChooserViewSet("person_chooser", url_prefix="person-chooser")
