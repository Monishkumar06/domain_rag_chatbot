# Domain-Specific RAG Chatbot for PDF Question Answering

## Overview

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on their content.

## Features

- PDF upload
- Page-wise text extraction
- Text chunking
- Sentence Transformer embeddings
- FAISS vector search
- Relevant document retrieval
- Groq LLM-based answers
- Source document and page display
- Fallback response for unavailable information
- Streamlit web interface

## Technologies Used

- Python
- Streamlit
- pypdf
- LangChain
- Sentence Transformers
- FAISS
- Groq
- python-dotenv

## Workflow

Upload PDF → Extract Text → Split into Chunks → Generate Embeddings → FAISS → Retrieve Relevant Chunks → Groq LLM → Answer + Source

## Installation

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1