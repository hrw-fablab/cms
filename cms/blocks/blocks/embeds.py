from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock


class EmbedsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    embed = EmbedBlock(required=False)

    class Meta:
        template = "blocks/embed.html"
        icon = "media"
