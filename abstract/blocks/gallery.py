from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class GalleryBlock(blocks.StructBlock):
	cards = blocks.ListBlock(ImageChooserBlock(required=False))

	class Meta:
		abstract=True