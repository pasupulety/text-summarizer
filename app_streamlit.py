import streamlit as st
import torch
from transformers import pipeline
st.set_page_config(
    page_title="AI Text Summarizer | Harshita Pasupulet",
    page_icon="🧠",
    layout="centered"
)


st.set_page_config(page_title="Text Summarizer", page_icon="🧠")

@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if device == "cuda" else -1)
    return summarizer

st.title("🧠 AI Text Summarizer")
st.markdown("""
### ✨ About this App  
This is an **AI-powered Text Summarizer** built using **Hugging Face Transformers (BART)** and **Streamlit**.  
It helps users quickly condense long text into short, meaningful summaries — ideal for reports, news, or research articles.
""")

st.write("Paste any long text below and let AI summarize it for you!")

# Load model
summarizer = load_model()

# Input text area
text = st.text_area("✍️ Paste your text here:", height=250)

# Parameters
min_len = st.slider("Minimum summary length", 20, 300, 60)
max_len = st.slider("Maximum summary length", 50, 500, 160)

if st.button("Summarize ✨"):
    if text.strip():
        with st.spinner("Summarizing... please wait ⏳"):
            summary = summarizer(text, min_length=min_len, max_length=max_len, do_sample=False)[0]['summary_text']
        st.subheader("✅ Summary:")
        st.write(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize!")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; font-size: 15px; color: gray;'>
        Developed with ❤️ by <b>Harshita Pasupulet</b><br>
        <a href='https://github.com/pasupulet-y/text-summarizer' target='_blank'>View on GitHub</a> |
        <a href='https://www.linkedin.com/in/harshitapasupulet/' target='_blank'>LinkedIn</a> |
        <a href='https://pasupulet-y-text-summarizer-app-streamlit-r8fjld.streamlit.app' target='_blank'>Live Demo</a>
    </div>
    """,
    unsafe_allow_html=True
)

