import argparse, sys, torch
from transformers import pipeline

def build_summarizer(model_name="facebook/bart-large-cnn", device=None):
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    return pipeline("summarization", model=model_name, device=0 if device=="cuda" else -1)

def read_text(args):
    if args.stdin:
        return sys.stdin.read()
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            return f.read()
    if args.text:
        return args.text
    raise SystemExit("No input provided. Use --input, --stdin, or --text.")

def main():
    p = argparse.ArgumentParser(description="Summarize long text using BART.")
    p.add_argument("--input", type=str, help="Path to .txt file")
    p.add_argument("--stdin", action="store_true", help="Read from STDIN")
    p.add_argument("--text", type=str, help="Inline text")
    p.add_argument("--min-length", type=int, default=60)
    p.add_argument("--max-length", type=int, default=160)
    p.add_argument("--num-beams", type=int, default=4)
    p.add_argument("--device", choices=["cpu","cuda"], default=None)
    args = p.parse_args()

    text = read_text(args).strip()
    summarizer = build_summarizer(device=args.device)
    out = summarizer(text, min_length=args.min_length, max_length=args.max_length,
                     num_beams=args.num_beams, do_sample=False, truncation=True)
    print(out[0]["summary_text"])

if __name__ == "__main__":
    main()
import argparse
import sys
import torch
from transformers import pipeline

# 🔧 Function to load the summarizer model
def build_summarizer(model_name="facebook/bart-large-cnn", device=None):
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    summarizer = pipeline("summarization", model=model_name, device=0 if device == "cuda" else -1)
    return summarizer, device

# 📥 Function to read text input from various sources
def read_text(args):
    if args.stdin:
        return sys.stdin.read()
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            return f.read()
    if args.text:
        return args.text
    raise SystemExit("❌ No input provided. Use --input, --stdin, or --text.")

# 🚀 Main function
def main():
    parser = argparse.ArgumentParser(description="Summarize long text using Hugging Face Transformers.")
    parser.add_argument("--input", type=str, help="Path to a .txt file to summarize")
    parser.add_argument("--stdin", action="store_true", help="Read text from STDIN")
    parser.add_argument("--text", type=str, help="Inline text to summarize")
    parser.add_argument("--min-length", type=int, default=60, help="Minimum summary length (tokens)")
    parser.add_argument("--max-length", type=int, default=160, help="Maximum summary length (tokens)")
    parser.add_argument("--num-beams", type=int, default=4, help="Beam search width")
    parser.add_argument("--device", type=str, choices=["cpu", "cuda"], default=None, help="Force device")
    parser.add_argument("--model", type=str, default="facebook/bart-large-cnn", help="Hugging Face model ID")
    args = parser.parse_args()

    text = read_text(args).strip()
    if not text:
        raise SystemExit("⚠️ Empty input text.")

    summarizer, device = build_summarizer(model_name=args.model, device=args.device)
    summary = summarizer(
        text,
        min_length=args.min_length,
        max_length=args.max_length,
        num_beams=args.num_beams,
        do_sample=False,
        truncation=True,
    )[0]["summary_text"]

    print("\n✅ Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
