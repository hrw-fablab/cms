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
    contain = blocks.BooleanBlock(required=False, label="Cointain Aspect Ratio", help_text="Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.")
    cards = GalleryCards()

    class Meta:
        group = "Cointainer"
        template = "templates/gallery.html"
        icon = "grip"
        abstract = True
