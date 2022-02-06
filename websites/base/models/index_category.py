from abstract.pages.index import AbstractIndexPage


class IndexCategoryPage(AbstractIndexPage):
    template = "pages/category.html"

    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["DevicePage", "ProjectPage"]

    class Meta:
        verbose_name = "Index Seite mit Kategorien"
