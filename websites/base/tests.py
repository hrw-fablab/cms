from wagtail.tests.utils import WagtailPageTests

from wagtail.core.models import Page

from websites.base.models import (
    CollectionPage,
    DeviceIndexPage,
    FlexPage,
    FolderPage,
    HomePage,
    IndexPage,
    ProjectIndexPage,
    SearchPage,
)


class HomePageTest(WagtailPageTests):
    def test_can_create(self):
        self.assertCanCreateAt(Page, HomePage)

    def test_subpage_types(self):
        self.assertAllowedSubpageTypes(
            HomePage,
            {
                Page,
                FolderPage,
                FlexPage,
                IndexPage,
                DeviceIndexPage,
                ProjectIndexPage,
                SearchPage,
                CollectionPage,
            },
        )

    def test_parentpage_types(self):
        self.assertAllowedParentPageTypes(
            HomePage,
            {Page},
        )


class FolderPageTest(WagtailPageTests):
    def test_can_create(self):
        self.assertCanCreateAt(HomePage, FolderPage)

    def test_subpage_types(self):
        self.assertAllowedSubpageTypes(
            FolderPage,
            {Page, FlexPage, IndexPage, DeviceIndexPage, ProjectIndexPage},
        )

    def test_parentpage_types(self):
        self.assertAllowedParentPageTypes(
            FolderPage,
            {HomePage},
        )


class FlexPageTest(WagtailPageTests):
    def test_can_create(self):
        self.assertCanCreateAt(HomePage, FlexPage)

    def test_subpage_types(self):
        self.assertAllowedSubpageTypes(
            FlexPage,
            {
                Page,
            },
        )

    def test_parentpage_types(self):
        self.assertAllowedParentPageTypes(
            FlexPage,
            {HomePage, FolderPage},
        )
