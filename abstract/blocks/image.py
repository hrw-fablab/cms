from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "molecules/media.html"
        icon = "image"
        abstract = True
