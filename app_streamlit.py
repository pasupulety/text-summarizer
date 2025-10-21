import streamlit as st
import torch
from transformers import pipeline

st.set_page_config(page_title="Text Summarizer", page_icon="🧠")

@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if device == "cuda" else -1)
    return summarizer

st.title("🧠 AI Text Summarizer")
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
