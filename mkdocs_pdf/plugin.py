from lxml.html import fromstring, tostring
from mkdocs.plugins import BasePlugin


class Plugin(BasePlugin):
    def on_page_content(self, html, page, config, files):
        """
        Searches for img tags with attribute type="application/pdf".
        Converts those tags to embed tags.
        """
        if not html:
            return html

        content = fromstring(html)
        tags = content.xpath(f'//img[@type="application/pdf" and @src]')
        for tag in tags:
            tag.tag = "embed"
        return tostring(content, encoding="unicode")
