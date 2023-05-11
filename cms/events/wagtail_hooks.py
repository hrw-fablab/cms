from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet

from .models import Event


class EventViewSet(SnippetViewSet):
    model = Event
    icon = "date"
    menu_label = "Event"
    menu_name = "events"
    add_to_admin_menu = True


register_snippet(EventViewSet)
