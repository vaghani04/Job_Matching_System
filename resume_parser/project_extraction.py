# parsing/projects_extraction.py
import re

def extract_projects(text):
    """Extract the 'Relevant Projects' section with full content until the next major header."""
    projects_pattern = re.compile(
        r'(RELEVANT PROJECTS|PROJECTS)(.*?)(?=(EDUCATION|SKILLS|ACHIEVEMENTS & CERTIFICATIONS|CERTIFICATIONS|$|\n[A-Z]+\n|\Z))', 
        re.DOTALL | re.IGNORECASE
    )
    match = projects_pattern.search(text)
    
    if match:
        projects_text = match.group(2).strip()
        return projects_text

    return None
