from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class Card(blocks.StructBlock):
	image = ImageChooserBlock(required=False)
	title = blocks.CharBlock(required=False)
	text = blocks.TextBlock(required=False)
	link_url = blocks.URLBlock(required=False)
	link_title = blocks.CharBlock(required=False)

class CardsBlock(blocks.StructBlock):
	cards = blocks.ListBlock(Card(), max_num=5)

	class Meta:
		abstract=True