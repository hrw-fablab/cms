from wagtail.core import blocks

from abstract.blocks import ProjectChooserBlock


class MembersBlock(blocks.StructBlock):
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

    members = ProjectChooserBlock(required=False)

    class Meta:
        group = "Cointainer"
        icon = "group"
        template = "templates/project.html"
        abstract = True
