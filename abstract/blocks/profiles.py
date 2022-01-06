from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class Profile(blocks.StructBlock):
	image = ImageChooserBlock(required=False)
	name = blocks.CharBlock(required=False)
	employment = blocks.ChoiceBlock(choices=[("SHK", "shk")],required=False)
	since = blocks.DateBlock(required=False)
	career = blocks.CharBlock(required=False)
	responsibility = blocks.CharBlock(required=False)
	expert = blocks.CharBlock(required=False)
	projects = blocks.CharBlock(required=False)
	description = blocks.CharBlock(required=False)

class ProfilesBlock(blocks.StructBlock):
	cards = blocks.ListBlock(Profile())

	class Meta:
		abstract=True