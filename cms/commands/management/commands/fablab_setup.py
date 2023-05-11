from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from wagtail.models import Page, Site

from cms.pages.models import (
    HomePage,
    FlexPage,
    DeviceIndexPage,
    FolderPage,
    FormPage,
    LinkPage,
    SearchPage,
    ArticleIndexPage,
    ProjectIndexPage,
)


class Command(BaseCommand):
    help = "Create basic Page Structure without Content"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wagtail_root = Page.get_first_root_node()
        self.fablab_root = None

    def create_page(self, title, Model, show_in_menus=False):
        content = ContentType.objects.get_for_model(Model)
        return Model(title=title, content_type=content, show_in_menus=show_in_menus)

    def add_page(self, root, page):
        root.add_child(instance=page)

    def add_pages(self, root, pages):
        for page in pages:
            self.add_page(root, page)

    def create_site(self, page):
        Site.objects.create(
            hostname="127.0.0.1",
            port=8000,
            root_page=page,
            is_default_site=True,
        )

    def handle(self, *args, **options):
        homepage = self.create_page("FabLab", HomePage)
        self.add_page(self.wagtail_root, homepage)
        self.create_site(homepage)

        # Set FabLab HomePage as root
        self.fablab_root = HomePage.objects.first()

        # Create Top Level Pages
        self.add_pages(
            self.fablab_root,
            [
                self.create_page("Termine", FlexPage, show_in_menus=True),
                self.create_page("Neuigkeiten", ArticleIndexPage, show_in_menus=True),
                self.create_page("Unser FabLab", FolderPage, show_in_menus=True),
                self.create_page("Dein Besuch", FolderPage, show_in_menus=True),
                self.create_page("Suche", SearchPage),
                self.create_page("Links", LinkPage),
            ],
        )

        # Create Sub Pages for "Unser FabLab"
        our_fablab_root = FolderPage.objects.get(title="Unser FabLab")
        self.add_pages(
            our_fablab_root,
            [
                self.create_page("Team", FlexPage, show_in_menus=True),
                self.create_page("Geräte", DeviceIndexPage, show_in_menus=True),
                self.create_page("Projekte", ProjectIndexPage, show_in_menus=True),
                self.create_page("Philosophie", FlexPage, show_in_menus=True),
                self.create_page("Geschichte", FlexPage, show_in_menus=True),
                self.create_page("Netzwerk", FlexPage, show_in_menus=True),
                self.create_page("Jobs und Praktika", FlexPage, show_in_menus=True),
                self.create_page("Spenden und Sponsoren", FlexPage, show_in_menus=True),
            ],
        )

        # Create Sub Pages for "Dein Besuch"
        your_visit_root = FolderPage.objects.get(title="Dein Besuch")
        self.add_pages(
            your_visit_root,
            [
                self.create_page("Anfahrt", FlexPage, show_in_menus=True),
                self.create_page("Offener Abend", FormPage, show_in_menus=True),
                self.create_page("Schulen", FlexPage, show_in_menus=True),
                self.create_page("Unternehmen", FlexPage, show_in_menus=True),
                self.create_page("StartUps", FlexPage, show_in_menus=True),
                self.create_page("FAQ", FlexPage, show_in_menus=True),
            ],
        )
