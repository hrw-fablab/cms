from wagtail import blocks
from django.contrib.sites.shortcuts import get_current_site
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    illustration = blocks.BooleanBlock(required=False)

    class Meta:
        template = "blocks/banner.html"
