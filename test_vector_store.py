from document_loader import load_pdf
from text_splitter import split_documents
from vector_store import create_vector_store

pdf_path = "documents/sample.pdf"

# Load PDF
documents = load_pdf(pdf_path)

# Split into chunks
chunks = split_documents(documents)

# Create vector store
index, model, stored_chunks = create_vector_store(chunks)

print("Embeddings created successfully!")
print("Total vectors stored:", index.ntotal)