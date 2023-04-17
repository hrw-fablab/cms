from wagtail import blocks
from.chooser import PersonChooserBlock


class PersonBlock(blocks.StructBlock):
    person = PersonChooserBlock(required=False)

    class Meta:
        template = "templates/person.html"
        icon = "user"
