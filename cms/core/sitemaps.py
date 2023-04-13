import inspect
from django.contrib.sitemaps import Sitemap as DjangoSitemap
from django.contrib.sitemaps import views as sitemap_views


# Custom Sitemap Generation to allow Google to read Multilangual Sites
class Sitemap(DjangoSitemap):
    def __init__(self, request=None):
        self.request = request

    def location(self, obj):
        return obj.localized.get_url(self.request)

    def lastmod(self, obj):
        # fall back on latest_revision_created_at if last_published_at is null
        # (for backwards compatibility from before last_published_at was added)
        return obj.last_published_at or obj.latest_revision_created_at

    def get_wagtail_site(self):
        from wagtail.models import Site

        site = Site.find_for_request(self.request)
        if site is None:
            return Site.objects.select_related("root_page").get(is_default_site=True)
        return site

    def items(self):
        return (
            self.get_wagtail_site()
            .root_page.get_descendants(inclusive=True)
            .live()
            .public()
            .order_by("path")
            .defer_streamfields()
            .specific()
        )


def index(request, sitemaps, **kwargs):
    sitemaps = prepare_sitemaps(request, sitemaps)
    return sitemap_views.index(request, sitemaps, **kwargs)


def sitemap(request, sitemaps=None, **kwargs):
    if sitemaps:
        sitemaps = prepare_sitemaps(request, sitemaps)
    else:
        sitemaps = {"wagtail": Sitemap(request)}
    return sitemap_views.sitemap(request, sitemaps, **kwargs)


def prepare_sitemaps(request, sitemaps):
    initialised_sitemaps = {}
    for name, sitemap_cls in sitemaps.items():
        if inspect.isclass(sitemap_cls) and issubclass(sitemap_cls, Sitemap):
            initialised_sitemaps[name] = sitemap_cls(request)
        else:
            initialised_sitemaps[name] = sitemap_cls
    return initialised_sitemaps


class FablabSiteMap(Sitemap):
    protocol = "https"
    i18n = True
    alternates = True
