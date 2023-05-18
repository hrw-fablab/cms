from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet

from .models import Project


class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = "tag"
    menu_label = "Projekt"
    list_display = ["name", "members_amount"]
    list_per_page = 40
    add_to_admin_menu = True


register_snippet(ProjectViewSet)