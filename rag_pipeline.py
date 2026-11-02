from document_loader import load_pdf
from text_splitter import split_documents
from vector_store import create_vector_store
from retriever import search_documents
from prompt import create_prompt


def setup_rag(pdf_path):
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    index, model, stored_chunks = create_vector_store(chunks)

    return index, model, stored_chunks


def ask_question(question, index, model, chunks):
    results = search_documents(
        question,
        index,
        model,
        chunks,
        top_k=3
    )

    context = "\n\n".join(
        result["text"] for result in results
    )

    prompt = create_prompt(question, context)

    return prompt, results