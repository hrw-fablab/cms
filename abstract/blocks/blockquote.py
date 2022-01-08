from wagtail.core import blocks

class BlockquoteBlock(blocks.StructBlock):
	text = blocks.TextBlock(required=False)
	cite = blocks.CharBlock(required=False)

	class Meta:
		abstract=True