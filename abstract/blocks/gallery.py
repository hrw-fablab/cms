from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class GalleryBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    cards = blocks.ListBlock(ImageChooserBlock(required=False))

    class Meta:
        abstract = True
