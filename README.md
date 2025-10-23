# 🧠 AI Text Summarizer

A simple **AI-powered text summarization app** built using **Hugging Face Transformers (BART)** and **Streamlit**.

---

### 🚀 Live Demo
🌐 [**Try it Here**](https://pasupulety-text-summarizer-app-streamlit-r8fjld.streamlit.app)
💻 [**View Source on GitHub**](https://github.com/pasupulety/text-summarizer)

---

### ✨ Features
- 🧾 Summarizes long text into concise summaries instantly.  
- ⚙️ Adjustable summary length (min and max sliders).  
- 🤖 Uses the **BART model** from Hugging Face Transformers.  
- ☁️ Deployed seamlessly using **Streamlit Cloud**.

---

### 🧩 Tech Stack
| Tool | Purpose |
|------|----------|
| 🐍 Python | Core programming language |
| 🤗 Hugging Face Transformers | NLP model for text summarization |
| 🔥 PyTorch | Deep learning backend |
| 🎨 Streamlit | Web app framework |

---

### 👩‍💻 Developed By
**Harshita Pasupulety**  
📍 Aspiring Data Analyst | AI & ML Enthusiast  
[LinkedIn](https://www.linkedin.com/in/harshitapasupulet/) • [Portfolio](#)  

---

### ⚡ Setup Instructions

Clone this repository and run locally:

```bash
# Clone the repository
git clone https://github.com/pasupulet-y/text-summarizer.git
cd text-summarizer

# (Optional) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app_streamlit.py
# 🧠 Text Summarizer
# 🧠 AI Text Summarizer

A simple **AI-powered text summarization app** built using **Hugging Face Transformers (BART)** and **Streamlit**.

🌐 **[Live Demo](https://pasupulet-y-text-summarizer-app-streamlit-r8fjld.streamlit.app)**  
📂 **[Source Code on GitHub](https://github.com/pasupulet-y/text-summarizer)**

---

### 🧩 Features
- Summarizes long text into concise summaries instantly.
- Adjustable summary length (min and max).
- Built using Hugging Face BART model.
- Deployed using Streamlit Cloud.

### 🛠️ Tech Stack
- Python
- Hugging Face Transformers
- Streamlit
- PyTorch

### 👩‍💻 Developed by
**Harshita Pasupulet**  
[LinkedIn](https://www.linkedin.com/in/harshitapasupulet/) | [Portfolio](#)


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
---

## 👩‍💻 Author

**Harshita Pasupulety**  
🎓 MPS in Analytics, Northeastern University  
💡 Passionate about Data Science, NLP, and AI-based innovations  
🔗 [GitHub](https://github.com/pasupulet-y) | [LinkedIn](https://www.linkedin.com/in/harshitapasupulety/)
