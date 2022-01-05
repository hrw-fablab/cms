from wagtail.core import blocks

class ParagraphBlock(blocks.StructBlock):
	title = blocks.CharBlock()
	text = blocks.RichTextBlock(features=['h3', 'ul', 'link', 'image', 'embed'])

	class Meta:
		abstract=True