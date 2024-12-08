import re

def extract_experience(text):
    """Extract years of experience from the job description text."""
    # A pattern to match experience requirements (e.g., "2-4 years", "5+ years")
    experience_pattern = r'(\d{1,2}[-+]\d{1,2}\s?years|\d{1,2}\s?years|\d\s?years)'
    experience = re.findall(experience_pattern, text)

    return experience if experience else ["No experience required"]
