from pypdf import PdfReader
def load_pdf(file_path):
    documents = []

    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            documents.append({
                "text": text,
                "page": page_number,
                "source": file_path
            })

    return documents