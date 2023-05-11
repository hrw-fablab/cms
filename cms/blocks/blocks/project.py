from wagtail import blocks
from wagtail.snippets import blocks as snippet_blocks


class ProjectMembers(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    layout = blocks.ChoiceBlock(
        choices=[
            ("extrem", "1 x N"),
            ("large", "2 x N"),
            ("medium", "3 x N"),
            ("small", "4 x N"),
        ],
        default="medium",
        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
    )

    members = snippet_blocks.SnippetChooserBlock("projects.Project", required=True)

    headings = blocks.BooleanBlock(
        required=False,
        label="Projektrollen Überschriften",
        help_text="Trenne Projektrollen durch Überschriften",
    )

    class Meta:
        group = "Content Grabber"
        icon = "group"
        template = "blocks/project.html"
