import streamlit as st
import tempfile
import os

from rag_pipeline import setup_rag, ask_question
from llm import generate_answer


st.set_page_config(
    page_title="Domain-Specific RAG Chatbot",
    page_icon="📚"
)

st.title("📚 Domain-Specific RAG Chatbot")
st.write("Upload a PDF and ask questions from the document.")


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    file_key = f"{uploaded_file.name}_{uploaded_file.size}"

    # Process PDF only when a new file is uploaded
    if st.session_state.get("file_key") != file_key:

        with st.spinner("Processing PDF..."):

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            )

            temp_file.write(uploaded_file.getbuffer())
            temp_file.close()

            try:
                index, model, chunks = setup_rag(
                    temp_file.name
                )

                st.session_state.index = index
                st.session_state.model = model
                st.session_state.chunks = chunks
                st.session_state.file_key = file_key
                st.session_state.file_name = uploaded_file.name

            finally:
                os.unlink(temp_file.name)

        st.success("PDF processed successfully! ✅")


    question = st.text_input(
        "Ask a question about the PDF:"
    )


    if st.button("Ask Question"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating answer..."):

                prompt, results = ask_question(
                    question,
                    st.session_state.index,
                    st.session_state.model,
                    st.session_state.chunks
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                answer = generate_answer(
                    question,
                    context
                )


            st.subheader("Answer")
            st.write(answer)


            st.subheader("📄 Source")

            pages = sorted(
                set(result["page"] for result in results)
            )

            st.write(
                f"Document: {st.session_state.file_name}"
            )

            st.write(
                "Page(s): " +
                ", ".join(str(page) for page in pages)
            )