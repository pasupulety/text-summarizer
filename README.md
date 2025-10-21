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
git clone https://github.com/pasupulet-y/text-summarizer.git
cd text-summarizer
python3 -m venv .venv
source .venv/bin/activate   # On Mac/Linux
# .venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python -m streamlit run app_streamlit.py
python summarize.py --input sample.txt --min-length 60 --max-length 160
text-summarizer/
│
├── app_streamlit.py      # Streamlit web app
├── summarize.py         # CLI summarizer script
├── sample.txt           # Sample input text
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
## 🛠️ Tech Stack
- **Language:** Python  
- **Framework:** Streamlit  
- **Model:** Hugging Face Transformers (BART)  
- **Tools:** Git, Virtualenv, CLI
## 🚀 Future Enhancements
- Add support for multiple summarization models (T5, Pegasus)
- Build a user-friendly web interface with more customization
- Enable file uploads (PDF/Text) for summarization
- Deploy using Streamlit Cloud or Hugging Face Spaces
## 📁 Project Structure
text-summarizer/
├── app_streamlit.py     # Streamlit web app
├── summarize.py         # CLI summarizer script
├── requirements.txt     # Python dependencies
├── sample.txt           # Sample input text
└── README.md            # Documentation
## 📊 Results & Demo
- Summarizes any text input with Hugging Face BART model.
- Easy to run via CLI or Streamlit web app.
- [Optional] Include a screenshot or GIF of the app if you have one.
