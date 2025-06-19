from transformers import pipeline

# Load once and reuse
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_with_t5(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        summary_piece = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        summary += summary_piece + "\n"
    return summary.strip()

def extract_bullet_points(text):
    lines = text.strip().split("\n")
    bullets = ["• " + line.strip().capitalize() for line in lines if len(line.strip()) > 30]
    return bullets
