from wagtail.core import blocks
from abstract.blocks.banner import BannerBlock

from abstract.blocks.grabber import GrabberBlock
from abstract.blocks.grid import GridBlock
from abstract.blocks.heading import HeadingBlock
from abstract.blocks.hero import HeroBlock
from abstract.blocks.html import HTMLBlock
from abstract.blocks.paragraph import ParagraphBlock
from abstract.blocks.person import PersonBlock
from abstract.blocks.spacer import SpacerBlock
from abstract.blocks.split import SplitBlock
from abstract.blocks.gallery import GalleryBlock
from abstract.blocks.blockquote import BlockquoteBlock
from abstract.blocks.image import ImageBlock
from abstract.blocks.video import VideoBlock
from abstract.blocks.embed import EmbedBlock
from abstract.blocks.card import CardBlock


class GridBlockElements(blocks.StreamBlock):
    card = CardBlock()
    person = PersonBlock()


class GridBlock(GridBlock):
    cards = GridBlockElements()


class HomeBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    hero = HeroBlock()
    split = SplitBlock()
    grid = GridBlock()
    grabber = GrabberBlock()
    gallery = GalleryBlock()
    blockquote = BlockquoteBlock()
    spacer = SpacerBlock()
    video = VideoBlock()
    image = ImageBlock()
    embed = EmbedBlock()
    card = CardBlock()
    person = PersonBlock()
    html = HTMLBlock()
    banner = BannerBlock()


class FlexBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    blockquote = BlockquoteBlock()
    split = SplitBlock()
    grid = GridBlock()
    grabber = GrabberBlock()
    spacer = SpacerBlock()
    gallery = GalleryBlock()
    video = VideoBlock()
    image = ImageBlock()
    embed = EmbedBlock()
    card = CardBlock()
    person = PersonBlock()
    html = HTMLBlock()
    banner = BannerBlock()