import streamlit as st

from pipeline import run_pipeline


# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Executive Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Executive Intelligence Copilot")

st.caption(
    "Upload a Monthly Executive Report and interact with its charts."
)

st.divider()


# --------------------------------------------------
# PDF Upload
# --------------------------------------------------

uploaded_pdf = st.file_uploader(
    "Upload Executive PDF Report",
    type=["pdf"]
)


# --------------------------------------------------
# Run Pipeline
# --------------------------------------------------

if uploaded_pdf is not None:

    st.success("PDF uploaded successfully.")

    with st.spinner("Processing report..."):

        result = run_pipeline(uploaded_pdf)

    st.divider()

    st.subheader("Pipeline Output")

    st.write(result)
