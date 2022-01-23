from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class GalleryCards(blocks.StreamBlock):
    image = ImageChooserBlock()
    video = VideoChooserBlock()
    embed = EmbedBlock()


class GalleryBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    
    cards = GalleryCards()

    class Meta:
        group = "Cointainer"
        template = "templates/gallery.html"
        icon = "grip"
        abstract = True
