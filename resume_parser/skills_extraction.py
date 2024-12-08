# parsing/skills_extraction.py
import re

def extract_skills(text):
    """Extract skills from the 'Technical Skills' section of the resume."""
    skills_section_pattern = re.compile(
        r'(TECHNICAL SKILLS|SKILLS)(.*?)(?=PROJECTS|CERTIFICATIONS|EDUCATION|CERTIFICATES|ACHIEVEMENTS|$)', 
        re.DOTALL | re.IGNORECASE
    )
    skills_section = skills_section_pattern.search(text)
    
    if skills_section:
        skills_text = skills_section.group(2)
        skills = re.split(r'[,\n•;]', skills_text)
        skills = [
            skill.strip() for skill in skills 
            if skill.strip() and not re.search(r'\b(?:\d{4}|\d{1,2}/\d{1,2}/\d{2,4})\b', skill.strip())
        ]
        return skills
    
    return None
