from core.models import FablabBasePage
from django.http import HttpResponseRedirect


class AbstractFolderPage(FablabBasePage):
    def serve(self, request):
        return HttpResponseRedirect("/")

    class Meta:
        verbose_name = "Ordner"
        abstract = True
