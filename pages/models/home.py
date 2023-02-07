from core.models import FablabBasePage


class HomePage(FablabBasePage):
    parent_page_types = ["wagtailcore.Page"]

    template = "pages/flex.html"

    class Meta:
        verbose_name = "Startseite"
