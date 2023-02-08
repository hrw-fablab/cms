from core.models import FablabBasePage


class ProjectIndexPage(FablabBasePage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ProjectPage"]

    template = "pages/category.html"

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            self.get_children().live().specific().order_by("-projectpage__category")
        )
        context["children"] = all_children
        return context

    class Meta:
        verbose_name = "Projekte"
