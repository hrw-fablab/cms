from core.models import FablabBasePage


class AbstractHomePage(FablabBasePage):
    parent_page_types = ["wagtailcore.Page"]

    class Meta:
        abstract = True
