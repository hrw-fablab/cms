from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.field_block import PageChooserBlock

class SplitBlock(blocks.StructBlock):
	title = blocks.TextBlock(required=False)
	text = blocks.TextBlock(required=False)
	link_title = blocks.CharBlock(required=False)
	link = PageChooserBlock(required=False)
	image = ImageChooserBlock()

	class Meta:
		abstract=True