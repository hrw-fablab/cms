from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock

class Card(blocks.StructBlock):
	image = ImageChooserBlock(required=False)
	title = blocks.CharBlock(required=False)
	text = blocks.TextBlock(required=False)
	link = LinkBlock(required=False)

class CardsBlock(blocks.StructBlock):
	title = blocks.CharBlock(required=False)
	cards = blocks.ListBlock(Card())

	class Meta:
		abstract=True