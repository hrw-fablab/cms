from wagtail.core import blocks
from django.contrib.sites.shortcuts import get_current_site
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    illustration = blocks.BooleanBlock(required=False)

    def get_template(self, context=None):
        if get_current_site(context["request"]).domain == "hrw-fablab":
            return "organisms/banner.html"
        return "organisms/banner.html"

    class Meta:
        abstract = True
