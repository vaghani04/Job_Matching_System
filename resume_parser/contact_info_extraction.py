# parsing/contact_info.py
import re

def extract_contact_info(text):
    """Extract email and phone numbers from text."""
    email = re.findall(r'\S+@gmail.com', text)
    phone = re.findall(r'\+?\d[\d -]{8,}\d', text)  # Regex for phone numbers
    return {"phone": phone}
