from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class Card(blocks.StructBlock):
	image = ImageChooserBlock(required=False)
	title = blocks.CharBlock(required=False)
	text = blocks.TextBlock(required=False)
	link_url = blocks.URLBlock(required=False)
	link_title = blocks.CharBlock(required=False)

class CardsBlock(blocks.StructBlock):
	title = blocks.CharBlock(required=False)
	cards = blocks.ListBlock(Card())

	class Meta:
		abstract=True