from wagtail.core import blocks

from abstract.blocks.articles import ArticlesBlock
from abstract.blocks.cards import CardsBlock
from abstract.blocks.heading import HeadingBlock
from abstract.blocks.hero import HeroBlock
from abstract.blocks.paragraph import ParagraphBlock
from abstract.blocks.profiles import ProfilesBlock
from abstract.blocks.split import SplitBlock
from abstract.blocks.gallery import GalleryBlock
from abstract.blocks.blockquote import BlockquoteBlock
from abstract.blocks.image import ImageBlock
from abstract.blocks.video import VideoBlock
from abstract.blocks.embed import EmbedBlock


class Hero(HeroBlock):
    class Meta:
        template = "organisms/hero.html"


class Split(SplitBlock):
    class Meta:
        template = "organisms/split.html"


class Cards(CardsBlock):
    class Meta:
        template = "templates/cards.html"


class Articles(ArticlesBlock):
    class Meta:
        template = "templates/articles.html"


class Heading(HeadingBlock):
    class Meta:
        template = "atoms/heading.html"


class Paragraph(ParagraphBlock):
    class Meta:
        template = "molecules/paragraph.html"


class Gallery(GalleryBlock):
    class Meta:
        template = "templates/gallery.html"


class Blockquote(BlockquoteBlock):
    class Meta:
        template = "molecules/blockquote.html"


class Profiles(ProfilesBlock):
    class Meta:
        template = "templates/profiles.html"


class Image(ImageBlock):
    class Meta:
        template = "molecules/media.html"


class Video(VideoBlock):
    class Meta:
        template = "molecules/media.html"


class Embed(EmbedBlock):
    class Meta:
        template = "molecules/media.html"


class HomeBlock(blocks.StreamBlock):
    heading = Heading()
    paragraph = Paragraph()
    hero = Hero()
    split = Split()
    cards = Cards()
    articles = Articles()
    gallery = Gallery()
    blockquote = Blockquote()
    video = Video()
    image = Image()
    embed = Embed()


class FlexBlock(blocks.StreamBlock):
    heading = Heading()
    paragraph = Paragraph()
    split = Split()
    cards = Cards()
    gallery = Gallery()
    blockquote = Blockquote()
    profiles = Profiles()
    video = Video()
    image = Image()
    embed = Embed()
