# parsing/tools_technologies_extraction.py
import re

def extract_tools_technologies(text):
    """Extract tools and technologies from the 'Tools & Technologies' section of the resume."""
    tools_tech_section_pattern = re.compile(
        r'(TOOLS AND TECHNOLOGIES|TOOLS & TECHNOLOGIES|TECHNOLOGIES)(.*?)(?=PROJECTS|CERTIFICATIONS|EDUCATION|CERTIFICATES|ACHIEVEMENTS|$)', 
        re.DOTALL | re.IGNORECASE
    )
    tools_tech_section = tools_tech_section_pattern.search(text)
    
    if tools_tech_section:
        tools_tech_text = tools_tech_section.group(2)
        tools_technologies = re.split(r'[,\n•;]', tools_tech_text)
        tools_technologies = [
            tool.strip() for tool in tools_technologies 
            if tool.strip() and not re.search(r'\b(?:\d{4}|\d{1,2}/\d{1,2}/\d{2,4})\b', tool.strip())
        ]
        return tools_technologies
    
    return None
