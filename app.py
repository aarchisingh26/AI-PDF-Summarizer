import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_with_t5, extract_bullet_points

st.set_page_config(page_title="PDF Analyzer + Summary", layout="wide")
st.title("PDF Analyzer + AI Summary Tool")

uploaded_file = st.file_uploader("Upload a PDF to summarize", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("📑 Extracted Text (Preview)")
        st.code(text[:1000] + "..." if len(text) > 1000 else text)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_with_t5(text)
            bullets = extract_bullet_points(summary)

            st.subheader("🧠 Summary")
            st.write(summary)

            st.subheader("✅ Bullet Points")
            for b in bullets:
                st.markdown(f"- {b}")
