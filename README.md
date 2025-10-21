# 🧠 Text Summarizer

A simple AI text summarizer built with Hugging Face Transformers (BART) and Streamlit.

## 🚀 Features
- 📊 Streamlit web app with min/max length sliders for text summarization.
- 🧑‍💻 CLI tool for summarizing text from the terminal.
- 🤗 Uses `facebook/bart-large-cnn` model from Hugging Face.

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/pasupulet-y/text-summarizer.git
cd text-summarizer
### 2️⃣ Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # On Mac/Linux
# .venv\Scripts\activate     # On Windows
pip install -r requirements.txt
python -m streamlit run app_streamlit.py
python summarize.py --input sample.txt --min-length 60 --max-length 160
