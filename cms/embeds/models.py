from wagtail.embeds.finders.base import EmbedFinder


class MatterportFinder(EmbedFinder):
    def __init__(self, **options):
        pass

    def accept(self, url):
        return bool("my.matterport.com/show/" in url)

    def find_embed(self, url, max_width=None):
        print("yes find")
        html = f'<iframe src="{url}" allowfullscreen loading="lazy" style="border: none"></iframe>'

        return {
            "title": "Matterport 3D Scan",
            "author_name": "Matterport",
            "provider_name": "Matterport",
            "type": "rich",
            "thumbnail_url": "",
            "width": 200,
            "height": 200,
            "html": html,
        }


class GoogleMapsFinder(EmbedFinder):
    def __init__(self, **options):
        pass

    def accept(self, url):
        return bool("google.com/maps/" in url)

    def find_embed(self, url, max_width=None):
        html = f'<iframe src="{url}" allowfullscreen loading="lazy" style="border: none"></iframe>'

        return {
            "title": "Google Maps",
            "author_name": "Google Maps",
            "provider_name": "Google Maps",
            "type": "rich",
            "thumbnail_url": "",
            "width": 200,
            "height": 200,
            "html": html,
        }
