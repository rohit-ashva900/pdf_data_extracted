import os
import fitz  # PyMuPDF
from google.cloud import vision


def extract_text_from_pdf(pdf_path):
    client = vision.ImageAnnotatorClient()

    document = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        pix = page.get_pixmap()
        img_byte_arr = pix.tobytes("png")

        image = vision.Image(content=img_byte_arr)
        response = client.document_text_detection(image=image)

        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        text += ''.join([symbol.text for symbol in word.symbols])
                        text += ' '

    return text
