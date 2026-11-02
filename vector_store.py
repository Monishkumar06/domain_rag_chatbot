from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


def create_vector_store(chunks):
    texts = [chunk["text"] for chunk in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(texts)

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, model, chunks