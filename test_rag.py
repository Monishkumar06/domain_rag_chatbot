from rag_pipeline import setup_rag, ask_question
from llm import generate_answer

pdf_path = "documents/sample.pdf"

index, model, chunks = setup_rag(pdf_path)

question = "What is RAG?"

prompt, results = ask_question(
    question,
    index,
    model,
    chunks
)

context = "\n\n".join(
    result["text"] for result in results
)

answer = generate_answer(question, context)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)

print("\nSOURCE:")
for result in results:
    print("Page:", result["page"])