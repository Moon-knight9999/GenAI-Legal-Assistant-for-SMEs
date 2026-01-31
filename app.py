import streamlit as st
import os

from ingestion.pdf_reader import read_pdf
from ingestion.docx_reader import read_docx
from ingestion.language_normalizer import normalize
from nlp.clause_extractor import extract_clauses
from risk_engine.clause_risk import score_clause

st.title("GenAI Legal Assistant for SMEs")

file = st.file_uploader(
    "Upload Contract",
    type=["pdf", "docx", "txt"]
)

if file is not None:
    file_name = file.name.lower()

    # --- READ FILE BASED ON EXTENSION ---
    if file_name.endswith(".pdf"):
        text = read_pdf(file)
    elif file_name.endswith(".docx"):
        text = read_docx(file)
    elif file_name.endswith(".txt"):
        text = file.read().decode("utf-8")
    else:
        st.error("Unsupported file format")
        st.stop()

    # --- NORMALIZE LANGUAGE (Hindi → English) ---
    text = normalize(text)

    # --- DEBUG: SHOW TEXT ---
    st.subheader("Extracted Text (Debug)")
    st.write(text[:2000])

    # --- CLAUSE EXTRACTION ---
    clauses = extract_clauses(text)

    st.subheader(f"Extracted Clauses ({len(clauses)})")

    for c in clauses:
        risk = score_clause(c)
        st.markdown(f"### Risk: {risk}")
        st.write(c)
