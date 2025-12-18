# 📊 CSV Profiler

![Python](https://img.shields.io/badge/Python-3.11+-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-UI-green) 
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**CSV Profiler** is an interactive Python tool for profiling CSV files.  
Upload your CSV, generate **Markdown** or **JSON** reports, and get insights instantly via a **Streamlit interface**.

---

## 🌟 Features

- ✅ Upload and profile CSV files easily
- ✅ Generate **Markdown** and **JSON** reports
- ✅ Interactive **Streamlit UI**
- ✅ Handles missing values, provides summary statistics
- ✅ Download reports for offline use

---

## 🚀 Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/AlhanoufAlswayed/BootCamp_Sdaia.git
cd BootCamp_Sdaia
python -m venv venv

## 🛠 Usage

### 1️⃣ Streamlit UI

```bash
streamlit run ui.py

---

```markdown
## 📁 Project Structure

BootCamp_Sdaia/
├── csv_profiler/ # Main package
│ ├── profile.py # CSV profiling logic
│ ├── render.py # JSON/Markdown rendering
│ ├── helper.py # Utility functions (numeric_stats, text_stats, is_missing, infer_type)
│ └── io.py # CSV reading
├── data/ # Input and output CSV files
├── output/ # Generated reports
├── ui.py # Streamlit interface
├── main.py # CLI script using Typer
├── requirements.txt # Dependencies
└── README.md
# Activate environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
# Install dependencies
pip install -r requirements.txt

