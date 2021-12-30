from wagtail.core import blocks

class ParagraphBlock(blocks.StructBlock):
	title = blocks.CharBlock()
	text = blocks.RichTextBlock()

	class Meta:
		abstract=True