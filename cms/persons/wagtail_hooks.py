from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet

from .models import Person


class PersonViewSet(SnippetViewSet):
    model = Person
    icon = "user"
    menu_label = "Person"
    list_display = ["first_name","last_name"]
    search_fields = ["first_name", "last_name"]
    add_to_admin_menu = True
    list_per_page = 40


register_snippet(PersonViewSet)
