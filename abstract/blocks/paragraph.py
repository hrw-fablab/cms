from wagtail.core import blocks

class ParagraphBlock(blocks.StructBlock):
	title = blocks.CharBlock(required=False)
	text = blocks.RichTextBlock(features=['h3', 'ul', 'link', 'image', 'embed', 'document-link'])

	class Meta:
		abstract=True