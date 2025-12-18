# 📊 CSV Profiler

![Python](https://img.shields.io/badge/Python-3.11+-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-UI-green) 
![Typer CLI](https://img.shields.io/badge/CLI-Typer-orange) 
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Streamlit UI](image.png)
**CSV Profiler** is a Python package and interactive tool for profiling CSV files.  
It provides both a **Streamlit UI** and **CLI** to generate **JSON** and **Markdown** reports with column statistics.

---

## 🌟 Features

- ✅ Profile CSV files quickly
- ✅ Generate **Markdown** and **JSON** reports
- ✅ Streamlit UI for interactive profiling
- ✅ CLI commands using Typer
- ✅ Handles missing values, detects column types
- ✅ Provides numeric and text statistics
- ✅ Download reports for offline use

---

## 🚀 Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/AlhanoufAlswayed/BootCamp_Sdaia.git
cd BootCamp_Sdaia
python -m venv venv
```

Activate the environment:

```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠 Usage

### 1️⃣ Streamlit UI

```bash
streamlit run ui.py
```

- Upload a CSV file
- Click **Profile CSV**
- View and download **Markdown** or **JSON** reports

### 2️⃣ Command-Line Interface (CLI)

```bash
# Greeting
python main.py greeting-user Alhanouf

# Farewell
python main.py goodbye Alhanouf --formal

# Profile CSV file
python main.py profile-csv data/input.csv data/report.json data/report.md
```

- Reads CSV file
- Profiles data using `basic_profile`
- Saves output in **JSON** and **Markdown**

---

## 📁 Project Structure

```
BootCamp_Sdaia/
├── csv_profiler/          # Main package
│   ├── profile.py         # CSV profiling logic
│   ├── render.py          # JSON/Markdown rendering
│   ├── helper.py          # Utility functions (numeric_stats, text_stats, is_missing, infer_type)
│   └── io.py              # CSV reading
├── data/                  # Input and output CSV files
├── output/                # Generated reports
├── ui.py                  # Streamlit interface
├── main.py                # CLI script using Typer
├── requirements.txt       # Dependencies
└── README.md
```

---

## 🧰 Technologies

- Python 3.11+
- Streamlit
- Typer CLI
- CSV handling (`csv`, `pandas`)
- JSON and Markdown rendering

---

## 👩‍💻 Author

**Alhanouf  Alswayed
