def search_documents(query, index, model, chunks, top_k=3):
    query_embedding = model.encode([query])
    query_embedding = query_embedding.astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        if i < len(chunks):
            results.append(chunks[i])

    return results