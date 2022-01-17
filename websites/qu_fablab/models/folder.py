from abstract.pages.folder import AbstractFolderPage


class QuFolderPage(AbstractFolderPage):
    parent_page_types = ["QuHomepage"]
    subpage_type = ["QuArticleIndexPage", "QuProjectIndexPage", "QuDeviceIndexPage"]

    class Meta:
        verbose_name = "Ordner Seite"
