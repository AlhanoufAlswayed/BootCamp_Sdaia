import csv
from io import StringIO
from pathlib import Path
import streamlit as st

from csv_profiler.profile import basic_profile
from csv_profiler.render import render_json, render_markdown


st.set_page_config(
    page_title="CSV Profiler",
    layout="wide",
    page_icon="📊"
)

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
        /* الواجهة العامة */
        .stApp {
            background-color: #ffffff;
            color: #6B7280;
        }

        body, p, span, label, div, h1, h2, h3, h4, h5, h6 {
            color: #6B7280 !important;
        }

        /* العنوان */
        .main-title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 10px;
            color: #4B5563 !important;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            color: #6B7280 !important;
        }

        /* الكرت */
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
        }

       /* زر Profile CSV يكون أسود */
.stButton>button {
    background-color: #111827 !important;
    color: #ffffff !important;
}

.stButton>button:hover {
    background-color: #000000 !important;
 }

        .stButton>button:hover {
            background-color: #1D4ED8;
        }

        /* ===== نتائج التحليل (أسود ناعم) ===== */
        .report-content,
        .report-content p,
        .report-content span,
        .report-content li,
        .report-content h1,
        .report-content h2,
        .report-content h3,
        .report-content h4 {
            color: #111827 !important;
        }

        .report-json {
            color: #111827 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HEADER ----------
st.markdown('<div class="main-title">📊 CSV Profiler</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload a CSV → Analyze it → Download reports</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📁 Upload a CSV file",
    type=["csv"]
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "report" not in st.session_state:
    st.session_state.report = None
if "report_json" not in st.session_state:
    st.session_state.report_json = None
if "report_md" not in st.session_state:
    st.session_state.report_md = None


# ---------- LOGIC ----------
if uploaded_file is not None:
    st.success("✅ File uploaded successfully")

    file_text = uploaded_file.getvalue().decode("utf-8", errors="replace")

    if st.button("🚀 Profile CSV"):
        rows = list(csv.DictReader(StringIO(file_text)))
        report = basic_profile(rows)

        st.session_state.report = report
        st.session_state.report_json = render_json(report)
        st.session_state.report_md = render_markdown(report)

    if st.session_state.report is not None:
        base = Path(uploaded_file.name).stem

        tab_md, tab_json = st.tabs(["📄 Markdown Report", "🧾 JSON Report"])

        with tab_md:
            st.download_button(
                "⬇️ Download Markdown",
                data=st.session_state.report_md,
                file_name=f"{base}.md",
                mime="text/markdown",
            )
            st.markdown(
                f'<div class="report-content">{st.session_state.report_md}</div>',
                unsafe_allow_html=True
            )

        with tab_json:
            st.download_button(
                "⬇️ Download JSON",
                data=st.session_state.report_json,
                file_name=f"{base}.json",
                mime="application/json",
            )
            st.markdown('<div class="report-json">', unsafe_allow_html=True)
            st.json(st.session_state.report)
            st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👆 Please upload a CSV file to get started")
