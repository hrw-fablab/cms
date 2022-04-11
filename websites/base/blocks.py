from wagtail.core import blocks

from abstract.blocks import (
    BannerBlock,
    GrabberBlock,
    GridBlock,
    HeadingBlock,
    HeroBlock,
    HTMLBlock,
    ParagraphBlock,
    PersonBlock,
    SpacerBlock,
    SplitBlock,
    GalleryBlock,
    BlockquoteBlock,
    ImageBlock,
    VideoBlock,
    EmbedBlock,
    CardBlock,
    MembersBlock
)


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
    members = MembersBlock()


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


class ProjectBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    blockquote = BlockquoteBlock()
    split = SplitBlock()
    grid = GridBlock()
    spacer = SpacerBlock()
    gallery = GalleryBlock()
    video = VideoBlock()
    image = ImageBlock()
    embed = EmbedBlock()
    html = HTMLBlock()
    banner = BannerBlock()
