from wagtail.core import blocks, telepath

from abstract.blocks.cards import CardsBlock
from abstract.blocks.heading import HeadingBlock
from abstract.blocks.hero import HeroBlock
from abstract.blocks.paragraph import ParagraphBlock
from abstract.blocks.split import SplitBlock

class Hero(HeroBlock):
	class Meta:
		template = "organisms/hero.html"

class Split(SplitBlock):
	class Meta:
		template = "organisms/split.html"

class Cards(CardsBlock):
	class Meta:
		template = "templates/cards.html"

class Heading(HeadingBlock):
	class Meta:
		template = "atoms/heading.html"

class Paragraph(ParagraphBlock):
	class Meta:
		template = "molecules/paragraph.html"

class StructBlock(blocks.StreamBlock):
	heading = Heading()
	paragraph = Paragraph()
	hero = Hero()
	split = Split()
	cards = Cards()