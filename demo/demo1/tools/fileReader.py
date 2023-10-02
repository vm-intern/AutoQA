import io
import tempfile

import docx
import pypdf
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import sys
sys.path.append('demo1')
from apps import bot

def read_docx(file):
    doc = docx.Document(file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)


def read_pdf(file):
    text = ""
    pdf_reader = pypdf.PdfReader(file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[0]
        text += page.extract_text()

    file.close()
    return text


def read_txt(file):

    text = ""
    for line in file:
        text += line.decode()
    return text


def read_epub(file):
    options = {"ignore_ncx": True}
    content = []
    with tempfile.NamedTemporaryFile(delete=False, suffix='.epub') as temp_file:
        for chunk in file.chunks():
            temp_file.write(chunk)
    book = epub.read_epub(temp_file.name, options)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Parse the HTML content using BeautifulSoup and remove tags
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text = soup.get_text()
            content.append(text)

    return '\n'.join(content)


def read_files(files):
    for file in files:
        format = str(file).split(".")[-1]
        if format == "pdf":
            bot.updatedb_from_string(read_pdf(file))
        elif format == "epub":
            bot.updatedb_from_string(read_epub(file))
        elif format == "docx":
            bot.updatedb_from_string(read_docx(file))
        elif format == "txt":
            bot.updatedb_from_string(read_txt(file))


if __name__ == '__main__':
    print("a")