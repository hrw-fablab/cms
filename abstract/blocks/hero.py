from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class HeroBlock(blocks.StructBlock):
	title = blocks.TextBlock(required=False)
	text = blocks.TextBlock(required=False)
	video = DocumentChooserBlock(required=False)
	image = ImageChooserBlock(required=False)

	class Meta:
		abstract=True