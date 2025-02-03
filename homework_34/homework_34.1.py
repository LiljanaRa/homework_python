import re


def extract_emails(text):
    pattern = r"(\w+\.?\w+@\w+.\w{2,})"
    matched_str = re.findall(pattern=pattern, string=text)

    return matched_str

text = "Contact us at info@example.com or support@example.com for assistance."

emails = extract_emails(text)

print(emails)