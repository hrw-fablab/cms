from wagtail.core import blocks
from .media import MediaBlock

class HeroBlock(blocks.StructBlock):
	title = blocks.TextBlock(required=False)
	text = blocks.TextBlock(required=False)
	media = MediaBlock(required=False)

	class Meta:
		abstract=True