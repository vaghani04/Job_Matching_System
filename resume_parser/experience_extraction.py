# parsing/experience_extraction.py
import re

def extract_experience(text):
    """Extract experience sections based on headers in uppercase."""
    experience_pattern = re.compile(
        r'(EXPERIENCE|EMPLOYMENT HISTORY|WORK HISTORY|PROFESSIONAL EXPERIENCE|CAREER SUMMARY)\s*[\n\r]+(.*?)(?=\n[A-Z\s]+\n|\Z)',
        re.DOTALL | re.IGNORECASE
    )
    matches = experience_pattern.findall(text)
    
    if matches:
        experience_texts = []
        for match in matches:
            header, content = match
            content = content.strip()
            if content:
                experience_texts.append(content)

        return "\n\n".join(experience_texts) if experience_texts else None

    return None
