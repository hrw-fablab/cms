from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import Page

# Create the base language redirection page which is responsible
# for redirecting the user to the, language specific, homepages
root = Page.get_first_root_node()
# Again, the LanguageRedirectionPage comes from the blog post
# linked to above.
language_redirection_page_content_type = ContentType.objects.get_for_model(
    LanguageRedirectionPage
)
# The source for model can be found here:
# https://www.codista.com/en/blog/wagtail-multi-language-and-internationalization/
language_redirection_page = LanguageRedirectionPage(
    title="codista.com",
    draft_title="codista.com",
    slug="root",
    content_type=language_redirection_page_content_type,
    show_in_menus=True
)
root.add_child(instance=language_redirection_page)
# Create a site with the new LanguageRedirectionPage set as the root
# Note: this is the wagtail Site model, not django's
Site.objects.create(
    hostname="localhost",
    root_page=language_redirection_page,
    is_default_site=True,
    site_name="codista.com",
)

