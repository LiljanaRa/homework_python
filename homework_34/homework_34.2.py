import re


def highlight_keywords(text, keywords):
    pattern = r'(\b' + "|".join(keywords) + r')\b'
    matched_str = re.sub(pattern=pattern, repl=r'*\1*', string=text, flags=re.I)
    return matched_str


text = "This is a sample text. We need to highlight Python and programming."

keywords = ["python", "programming"]

highlighted_text = highlight_keywords(text, keywords)

print(highlighted_text)