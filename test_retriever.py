from document_loader import load_pdf
from text_splitter import split_documents
from vector_store import create_vector_store
from retriever import search_documents

pdf_path = "documents/sample.pdf"

documents = load_pdf(pdf_path)
chunks = split_documents(documents)

index, model, stored_chunks = create_vector_store(chunks)

query = "What is RAG?"

results = search_documents(
    query,
    index,
    model,
    stored_chunks
)

print("Question:", query)
print("\nRetrieved results:")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Page:", result["page"])
    print(result["text"])
    