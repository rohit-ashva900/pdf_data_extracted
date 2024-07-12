import os
from pdf_scanner import extract_text_from_pdf
from image_scanner import extract_text_from_image


def bulk_scan_documents(directory_path):
    data_model = {}

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            text = extract_text_from_image(file_path)
        else:
            continue

        data_model[filename] = text

    return data_model
