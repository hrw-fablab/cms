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
    ProjectMembers,
)


class GridBlockElements(blocks.StreamBlock):
    card = CardBlock(label="Karte")
    person = PersonBlock(label="Person")


class GridBlock(GridBlock):
    cards = GridBlockElements(label="Grid Elemente")


class HomeBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
    hero = HeroBlock(label="Hero")
    split = SplitBlock(label="Split")
    grid = GridBlock(label="Grid")
    grabber = GrabberBlock(label="Seiten Inhalte")
    gallery = GalleryBlock(label="Galerie")
    blockquote = BlockquoteBlock(label="Zitat")
    spacer = SpacerBlock(label="Spacer")
    video = VideoBlock(label="Video")
    image = ImageBlock(label="Bild")
    embed = EmbedBlock(label="Website einbetten")
    card = CardBlock(label="Card")
    person = PersonBlock(label="Person")
    html = HTMLBlock(label="HTML")
    banner = BannerBlock(label="Banner")
    project = ProjectMembers(label="Projekt Mitglieder")


class FlexBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
    split = SplitBlock(label="Split")
    grid = GridBlock(label="Grid")
    grabber = GrabberBlock(label="Seiten Inhalte")
    gallery = GalleryBlock(label="Galerie")
    blockquote = BlockquoteBlock(label="Zitat")
    spacer = SpacerBlock(label="Spacer")
    video = VideoBlock(label="Video")
    image = ImageBlock(label="Bild")
    embed = EmbedBlock(label="Website einbetten")
    card = CardBlock(label="Card")
    person = PersonBlock(label="Person")
    html = HTMLBlock(label="HTML")
    banner = BannerBlock(label="Banner")
    project = ProjectMembers(label="Projekt Mitglieder")


class ProjectBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
    split = SplitBlock(label="Split")
    grid = GridBlock(label="Grid")
    gallery = GalleryBlock(label="Galerie")
    blockquote = BlockquoteBlock(label="Zitat")
    spacer = SpacerBlock(label="Spacer")
    video = VideoBlock(label="Video")
    image = ImageBlock(label="Bild")
    embed = EmbedBlock(label="Website einbetten")
    card = CardBlock(label="Card")
    html = HTMLBlock(label="HTML")
    banner = BannerBlock(label="Banner")
    project = ProjectMembers(label="Projekt Mitglieder")
