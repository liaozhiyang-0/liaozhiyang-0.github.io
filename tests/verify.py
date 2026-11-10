"""Dependency-free structural checks. Run from the repository root."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))


class SiteChecks(unittest.TestCase):
    def test_page(self):
        page = Page()
        page.feed(Path('index.html').read_text(encoding='utf-8'))
        ids = [attrs['id'] for _, attrs in page.nodes if 'id' in attrs]
        self.assertEqual(len(ids), len(set(ids)), 'Duplicate IDs')
        self.assertEqual(sum(tag == 'h1' for tag, _ in page.nodes), 1)
        self.assertTrue(any(tag == 'html' and attrs.get('lang') == 'en' for tag, attrs in page.nodes))
        for tag, attrs in page.nodes:
            if 'data-en' in attrs or 'data-zh' in attrs:
                self.assertTrue(attrs.get('data-en'))
                self.assertTrue(attrs.get('data-zh'))
            for key in ('href', 'src'):
                value = attrs.get(key, '')
                if not value:
                    continue
                if value.startswith('#'):
                    self.assertTrue(value == '#' or value[1:] in ids, value)
                elif not urlsplit(value).scheme:
                    self.assertTrue(Path(value).is_file(), value)
                else:
                    self.assertEqual(urlsplit(value).scheme, 'https', value)
        for key in ('description', 'viewport'):
            self.assertTrue(any(tag == 'meta' and attrs.get('name') == key and attrs.get('content') for tag, attrs in page.nodes))
        for key in ('og:title', 'og:description', 'og:type'):
            self.assertTrue(any(attrs.get('property') == key and attrs.get('content') for _, attrs in page.nodes))
        self.assertTrue(Path('.nojekyll').exists())
        name = next(attrs for _, attrs in page.nodes if attrs.get('id') == 'profile-name')
        self.assertEqual(name.get('data-en'), 'Zhiyang Liao')
        self.assertEqual(name.get('data-zh'), '廖志洋')
        canonical = next(attrs for tag, attrs in page.nodes if tag == 'link' and attrs.get('rel') == 'canonical')
        self.assertEqual(canonical['href'], 'https://liaozhiyang-0.github.io/')


if __name__ == '__main__':
    unittest.main()
