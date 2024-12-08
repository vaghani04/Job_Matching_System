import re

def extract_certifications(text):
    """Extract all lines from the certifications section."""
    certifications_pattern = re.compile(
        r'(certifications?|courses?|accreditations?|certificates?|achievements?)'
        r'([\s\S]*?)(certificates|achievements|$)',
        re.IGNORECASE
    )
    
    matches = certifications_pattern.findall(text)
    
    if matches:
        certifications_content = matches[0][1].strip()
        certifications_lines = [line.strip() for line in certifications_content.splitlines() if line.strip()]
        return "\n".join(certifications_lines)

    return None