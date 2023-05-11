from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet

from .models import Project


class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = "tag"
    menu_label = "Project"
    menu_name = "projects"
    add_to_admin_menu = True


register_snippet(ProjectViewSet)
