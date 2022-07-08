from wagtail import blocks

class NewsletterBlock(blocks.StructBlock):

    class Meta:
        template = "molecules/newsletter.html"
        icon = "image"
        abstract = True
