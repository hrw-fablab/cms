from wagtail.core import blocks
from .media import MediaBlock
from wagtail_link_block.blocks import LinkBlock

class SplitBlock(blocks.StructBlock):
	title = blocks.TextBlock(required=False)
	text = blocks.TextBlock(required=False)
	link = LinkBlock(required=False)
	media = MediaBlock(required=False)

	class Meta:
		abstract=True