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

# ======================================================
# Report Summary
# ======================================================

    st.subheader("📄 Report Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Pages",
            result["pages"]["total_pages"]
        )

    with col2:
        st.metric(
            "Executive Charts",
            result["repository"]["total_charts"]
        )

    st.divider()

# ======================================================
# Executive Chart Inventory
# ======================================================

    st.subheader("📊 Executive Chart Inventory")

    for chart in result["repository"]["charts"]:

        with st.container(border=True):

            c1, c2 = st.columns([1, 4])

            with c1:

                st.markdown(f"### {chart['chart_id']}")

            with c2:

                st.markdown(
                    f"**{chart['chart_title']}**"
                )

                st.write(
                    f"📄 Page : {chart['page_number']}"
                )

                st.write(
                    f"📈 Type : {chart['chart_type']}"
                )

                st.write(
                    f"🏭 Area : {chart['business_area']}"
                )

                st.write(
                    chart["summary"]
                )

                st.caption(
                    f"Confidence : {chart['confidence']:.2f}"
                )


    st.subheader("Pipeline Output")

    st.write(result)
