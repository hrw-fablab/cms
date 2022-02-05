from abstract.pages.search import AbstractSearchPage


class QuSearchPage(AbstractSearchPage):
    template = "pages/search.html"

    parent_page_types = ["QuHomepage"]
    subpage_type = []

    class Meta:
        verbose_name = "Such Seite"
