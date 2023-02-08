from core.models import FablabBasePage
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from blocks.models import HomeBlock


class HomePage(FablabBasePage):
    subpage_type = [
        "FolderPgae",
        "FlexPage",
        "IndexPage",
        "DeviceIndexPage",
        "ProjectIndexPage",
        "SearchPage",
        "CollectionPage",
        "FormPage",
    ]

    template = "pages/flex.html"

    body = StreamField(HomeBlock(), blank=True, use_json_field=True)

    content_panels = FablabBasePage.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Startseite"
