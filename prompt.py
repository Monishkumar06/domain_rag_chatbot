def create_prompt(question, context):
    prompt = f"""
You are a PDF question-answering assistant.

Answer the question ONLY using the provided context.

If the answer is not available in the context, say:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt