from wagtail import blocks
from wagtail.contrib.table_block.blocks import TableBlock


class TableBlock(blocks.StructBlock):
    table = TableBlock(required=False)

    class Meta:
        template = "molecules/table.html"
