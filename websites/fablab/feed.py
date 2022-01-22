from django.contrib.syndication.views import Feed
from .models import ArticlePage


class RssFeed(Feed):
    title = "HRW-Fablab Neuigkeiten"
    link = "feed/"

    def items(self):
        return ArticlePage.objects.live().public().order_by("-date")[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.introduction

    def item_link(self, item):
        return item.full_url

    def item_pubdate(self, item):
        return item.first_published_at