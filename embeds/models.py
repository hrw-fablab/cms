from requests import request
from wagtail.embeds.finders.base import EmbedFinder


class MatterportFinder(EmbedFinder):
    def __init__(self, **options):

        pass

    def accept(self, url):
        """
        Returns True if this finder knows how to fetch an embed for the URL.

        This should not have any side effects (no requests to external servers)
        """

        print(bool("matterport.com" in url))
        return bool("matterport.com" in url)

    def find_embed(self, url, max_width=None):
        """
        Takes a URL and max width and returns a dictionary of information about the
        content to be used for embedding it on the site.

        This is the part that may make requests to external APIs.
        """
        # TODO: Perform the request

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
