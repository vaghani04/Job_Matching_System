import re

def clean_text(text):
    """Clean and preprocess the text data (remove special characters, stop words, etc.)."""
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    return text

def remove_bullets(text):
    """Remove common bullet points and symbols from text."""
    text = re.sub(r'^\s*[-•*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n\s*[-•*]\s+', '\n', text)
    return text
