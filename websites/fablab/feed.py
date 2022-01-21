from django.contrib.syndication.views import Feed
from .models import ArticlePage


class RssFeed(Feed):
    title = "HRW-Fablab"
    link = "feed/"
    description = "HRW-Fablab"
    feed_url = "/feed/"

    language = "de"

    def items(self):
        return ArticlePage.objects.order_by("-date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.introduction

    def item_link(self, item):
        return item.full_url

    def item_pubdate(self, item):
        return item.first_published_at