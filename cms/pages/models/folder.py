from cms.core.models import FablabBasePage
from django.http import HttpResponseRedirect


class FolderPage(FablabBasePage):
    parent_page_types = ["HomePage"]
    subpage_type = ["FlexPage", "IndexPage", "DeviceIndexPage", "ProjectIndexPage"]

    def serve(self, request):
        return HttpResponseRedirect("/")

    class Meta:
        verbose_name = "Ordner"
