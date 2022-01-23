from wagtail.core import blocks

class GridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    
    class Meta:
        group = "Cointainer"
        template = "templates/grid.html"
        icon = "grip"
        abstract = True
