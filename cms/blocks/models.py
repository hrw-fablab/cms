from wagtail import blocks

from .blocks import (
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
    EmbedsBlock,
    CardBlock,
    ProjectMembers,
    TableBlock,
    EventsBlock,
    CalendarBlock,
    CallBlock,
)


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
    embed = EmbedsBlock(label="Website einbetten")
    card = CardBlock(label="Card")
    person = PersonBlock(label="Person")
    html = HTMLBlock(label="HTML")
    banner = BannerBlock(label="Banner")
    project = ProjectMembers(label="Projekt Mitglieder")
    table = TableBlock(label="Tabelle")
    calendar = CalendarBlock(label="Kalendar")
    call = CallBlock(label="Call to Action")
    events = EventsBlock(label="")


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
    embed = EmbedsBlock(label="Website einbetten")
    card = CardBlock(label="Card")
    person = PersonBlock(label="Person")
    html = HTMLBlock(label="HTML")
    banner = BannerBlock(label="Banner")
    project = ProjectMembers(label="Projekt Mitglieder")
    table = TableBlock(label="Tabelle")
    calendar = CalendarBlock(label="Kalendar")
    call = CallBlock(label="Call to Action")
    events = EventsBlock(label="")


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
    embed = EmbedsBlock(label="Website einbetten")
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
    embed = EmbedsBlock(label="Website einbetten")
    html = HTMLBlock(label="HTML")
    table = TableBlock(label="Tabelle")


class FormBlock(blocks.StreamBlock):
    heading = HeadingBlock(label="Überschrift")
    paragraph = ParagraphBlock(label="Absatz")
    split = SplitBlock(label="Split")
    grid = GridBlock(label="Grid")
    gallery = GalleryBlock(label="Galerie")
    banner = BannerBlock(label="Banner")
    video = VideoBlock(label="Video")
    image = ImageBlock(label="Bild")
    embed = EmbedsBlock(label="Website einbetten")
