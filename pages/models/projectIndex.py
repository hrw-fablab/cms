from core.models import FablabBasePage


class ProjectIndexPage(FablabBasePage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ProjectPage"]

    template = "pages/projects.html"

    def get_context(self, request):
        context = super().get_context(request)
        children = self.get_children().live().specific()
        context["children"] = children
        return context

    class Meta:
        verbose_name = "Projekte"
