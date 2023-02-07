from core.models import FablabBasePage
from django.contrib.sites.shortcuts import get_current_site


class FlexPage(FablabBasePage):
    def get_template(self, request, *args, **kwargs):
        if get_current_site(request).domain == "hrw-fablab":
            return "pages/flex.html"
        return "pages/flex.html"

    class Meta:
        verbose_name = "Flexible Seite"
