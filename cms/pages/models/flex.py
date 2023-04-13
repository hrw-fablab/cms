from core.models import FablabBasePage
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from blocks.models import FlexBlock


class FlexPage(FablabBasePage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = []

    template = "pages/flex.html"

    body = StreamField(FlexBlock(), blank=True, use_json_field=True)

    content_panels = FablabBasePage.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flexible Seite"
