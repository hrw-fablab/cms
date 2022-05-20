from wagtail import blocks
from abstract.blocks import PersonChooserBlock


class PersonBlock(blocks.StructBlock):
    person = PersonChooserBlock(required=False)

    class Meta:
        template = "templates/person.html"
        icon = "user"
        abstract = True
