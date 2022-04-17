from wagtail.core import blocks

class GridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    layout = blocks.ChoiceBlock(choices = [
        ("extrem", "1 x N"),
        ("large", "2 x N"),
        ("medium", "3 x N"),
        ("small", "4 x N"),
    ], default="medium", help_text="Die Anzahl an Elementen in einer Horizontalen Reihe")
    
    class Meta:
        group = "Cointainer"
        template = "templates/grid.html"
        icon = "grip"
        abstract = True
