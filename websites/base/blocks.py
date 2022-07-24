from cProfile import label
from wagtail import blocks

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
    TableBlock,
)
from abstract.blocks.calender import CalendarBlock
from abstract.blocks.call import CallBlock


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
    table = TableBlock(label="Tabelle")
    calendar = CalendarBlock(label="Kalendar")
    call = CallBlock(label="Call to Action")


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
    table = TableBlock(label="Tabelle")
    calendar = CalendarBlock(label="Kalendar")
    call = CallBlock(label="Call to Action")


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
    table = TableBlock(label="Tabelle")


class DeviceBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
    split = SplitBlock(label="Split")
    grid = GridBlock(label="Grid")
    gallery = GalleryBlock(label="Galerie")
    spacer = SpacerBlock(label="Spacer")
    video = VideoBlock(label="Video")
    image = ImageBlock(label="Bild")
    embed = EmbedBlock(label="Website einbetten")
    html = HTMLBlock(label="HTML")
    table = TableBlock(label="Tabelle")


class FormBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
