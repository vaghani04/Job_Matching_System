import re

def extract_name(text):
    """Extract the candidate's name from the resume text."""
    # Basic regex pattern to detect possible name formats.
    name_pattern = r'(?<=\bName:\s)([A-Za-z\s]+)'
    match = re.search(name_pattern, text)

    if match:
        return match.group(1).strip()
    else:
        return "Name not found"
