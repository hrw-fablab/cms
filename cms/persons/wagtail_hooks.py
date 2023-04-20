from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from .models import Person

class PersonViewSet(SnippetViewSet):
    model = Person
    icon = "user"
    menu_label = "User"
    menu_name = "users"
    add_to_admin_menu = True

register_snippet(PersonViewSet)