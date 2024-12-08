# parsing/education_extraction.py
import re
from text_processing import remove_bullets

def extract_education(text):
    """Extract education details."""
    education_pattern = re.compile(r'(B\.Sc|B\.Eng|M\.Sc|M\.Eng|Bachelor|Master|Ph\.D|Doctorate|Diploma).*?(Computer Science|Engineering|Data Science|Information Technology|Business|Mathematics)', re.DOTALL | re.IGNORECASE)
    education_text = education_pattern.findall(text)
    return [remove_bullets(item) for sublist in education_text for item in sublist]
