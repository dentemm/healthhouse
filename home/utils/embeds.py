from wagtail.embeds.finders.base import EmbedFinder

class GoogleForms(EmbedFinder):

    def accept(self, url):
        """
        Returns True if this finder knows how to fetch an embed for the URL.

        This should not have any side effects (no requests to external servers)
        """
        return True

    def find_embed(self, url, max_width=None):
        """
        Takes a URL and max width and returns a dictionary of information about the
        content to be used for embedding it on the site.

        This is the part that may make requests to external APIs.
        """
        # TODO: Perform the request

        return {
            'title': "Google Form",
            'author_name': "Health House",
            'provider_name': "Google",
            'type': "rich",
            'thumbnail_url': "URL to thumbnail image",
            'width': 640,
            'height': 482,
            'html': '''<iframe src="{0}" width="640" height="482" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>'''.format(url)
        }