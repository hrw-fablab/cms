from wagtail.core import blocks

from abstract.blocks.cards import CardsBlock
from abstract.blocks.hero import HeroBlock
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

class StructBlock(blocks.StreamBlock):
	heading = blocks.CharBlock()
	hero = Hero()
	split = Split()
	cards = Cards()