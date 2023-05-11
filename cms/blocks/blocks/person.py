from wagtail import blocks
from wagtail.snippets import blocks as snippet_blocks


class PersonBlock(blocks.StructBlock):
    person = snippet_blocks.SnippetChooserBlock("persons.Person", required=False)

    class Meta:
        template = "templates/person.html"
        icon = "user"
