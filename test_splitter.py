from document_loader import load_pdf
from text_splitter import split_documents

pdf_path = "documents/sample.pdf"

documents = load_pdf(pdf_path)
chunks = split_documents(documents)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\nChunk", i + 1)
    print("Page:", chunk["page"])
    print(chunk["text"])