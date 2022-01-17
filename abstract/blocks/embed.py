from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock


class EmbedBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    embed = EmbedBlock(required=False)

    class Meta:
        icon = "media"
        abstract = True
