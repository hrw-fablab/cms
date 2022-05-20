from wagtail.test.utils import WagtailPageTests
from wagtail.test.utils.form_data import nested_form_data, streamfield
from wagtail.models import Page, Site

from websites.base.models import (
    CollectionPage,
    DeviceIndexPage,
    FlexPage,
    FolderPage,
    FormPage,
    HomePage,
    IndexPage,
    ProjectIndexPage,
    SearchPage,
)


class HomePageTest(WagtailPageTests):
    def test_parentpage_types(self):
        self.assertAllowedParentPageTypes(
            HomePage,
            {Page},
        )

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
                FormPage,
            },
        )

    def test_can_create(self):
        self.assertCanCreateAt(Page, HomePage)

    def test_can_create_title(self):
        root_page = Page.objects.get(pk=1)
        self.assertCanCreate(
            root_page,
            HomePage,
            nested_form_data(
                {
                    "title": "HomePage",
                    "og_type": "website",
                    "tw_size": "summary",
                    "index": "index",
                    "body": streamfield([]),
                },
            ),
        )

    def test_can_create_streamfield(self):
        root_page = Page.objects.get(pk=1)
        self.assertCanCreate(
            root_page,
            HomePage,
            nested_form_data(
                {
                    "title": "HomePage",
                    "og_type": "website",
                    "tw_size": "summary",
                    "index": "index",
                    "body": streamfield([("heading", "Test Heading")]),
                },
            ),
        )


class FolderPageTest(WagtailPageTests):
    def test_parentpage_types(self):
        self.assertAllowedParentPageTypes(
            FolderPage,
            {HomePage},
        )

    def test_subpage_types(self):
        self.assertAllowedSubpageTypes(
            FolderPage,
            {Page, FlexPage, IndexPage, DeviceIndexPage, ProjectIndexPage, FormPage},
        )

    def test_can_create(self):
        self.assertCanCreateAt(HomePage, FolderPage)
