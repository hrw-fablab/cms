from wagtail.core import blocks
from wagtail.core.blocks.field_block import PageChooserBlock

class ArticlesBlock(blocks.StructBlock):
	title = blocks.CharBlock(required=False)
	pages = blocks.ListBlock(PageChooserBlock())

	class Meta:
		abstract=True