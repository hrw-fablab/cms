from wagtail.images.formats import Format, register_image_format

register_image_format(
    Format("centered", "Mittig", "richtext-image centered", "max-600x500")
)
