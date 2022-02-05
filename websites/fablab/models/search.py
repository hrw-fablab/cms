from abstract.pages.search import AbstractSearchPage


class SearchPage(AbstractSearchPage):
    template = "pages/search.html"

    parent_page_types = ["Homepage"]
    subpage_type = []

    class Meta:
        verbose_name = "Such Seite"
