from document_loader import load_pdf

pdf_path = "documents/sample.pdf"

documents = load_pdf(pdf_path)

print("Total pages extracted:", len(documents))

for doc in documents:
    print("\nPage:", doc["page"])
    print(doc["text"][:200])