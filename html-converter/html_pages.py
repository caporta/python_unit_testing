import html as html_converter


class HtmlPagesConverter:
    def __init__(self, file_access):
        self.file_access = file_access
        self.breaks = [0]
        with self.file_access.open() as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if 'PAGE_BREAK' in line:
                    page_break_position = f.tell()
                    self.breaks.append(page_break_position)
            self.breaks.append(f.tell())

    def get_html_page(self, page):
        page_start = self.breaks[page]
        page_end = self.breaks[page + 1]
        html = ''
        with self.file_access.open() as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if 'PAGE_BREAK' in line:
                    continue
                html += html_converter.escape(line, quote=True)
                html += '<br />'
        return html


class FileAccessWrapper:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        return open(self.filename, 'r', encoding='utf-8')
