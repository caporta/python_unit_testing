import unittest
import os
import tempfile

from .html_pages import HtmlPagesConverter, FileAccessWrapper


class HtmlPagesTest(unittest.TestCase):
    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), 'afile.txt')
        f = open(filename, 'w', encoding='utf-8')
        f.write('plain text\n')
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        new_text = converter.get_html_page(0)
        self.assertEqual('plain text<br />', new_text)
