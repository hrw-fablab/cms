from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class SplitBlock(blocks.StructBlock):
	title = blocks.TextBlock(required=False)
	text = blocks.TextBlock(required=False)
	link_url = blocks.URLBlock(required=False)
	link_title = blocks.CharBlock(required=False)
	image = ImageChooserBlock()

	class Meta:
		abstract=True