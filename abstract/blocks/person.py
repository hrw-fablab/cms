from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    name = blocks.CharBlock(required=False)
    employment = blocks.ChoiceBlock(choices=[("SHK", "shk")], required=False)
    since = blocks.DateBlock(required=False)
    career = blocks.CharBlock(required=False)
    responsibility = blocks.CharBlock(required=False)
    expert = blocks.CharBlock(required=False)
    projects = blocks.CharBlock(required=False)
    description = blocks.TextBlock(required=False)

    class Meta:
        template = "templates/person.html"
        icon = "user"
        abstract = True