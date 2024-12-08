import re

def extract_skills(text):
    """Extract skills from the job description text."""
    # Use regex to dynamically identify the 'Skills' section in the JD
    skills_section_pattern = re.compile(
        r'(SKILLS|TECHNICAL SKILLS|REQUIREMENTS|QUALIFICATIONS)(.*?)(?=RESPONSIBILITIES|EXPERIENCE|EDUCATION|$)',
        re.DOTALL | re.IGNORECASE
    )
    skills_section = skills_section_pattern.search(text)

    # If a 'Skills' section is found, process it
    if skills_section:
        skills_text = skills_section.group(2)
        # Normalize text and remove bullets
        skills_text = re.sub(r'[\n\r]', ' ', skills_text)  # Replace newlines with spaces
        skills_text = re.sub(r'\b\d{1,2}\s?years\b', '', skills_text, flags=re.IGNORECASE)  # Remove year mentions
        skills_text = re.sub(r'[\u2022\u25E6\u25AA\u25CF]', '', skills_text)  # Remove bullet symbols

        # Split skills based on common delimiters
        skills = re.split(r'[;,\n\r]', skills_text)
        skills = [
            skill.strip() for skill in skills
            if skill.strip() and len(skill.strip()) > 1
        ]
        return list(set(skills))  # Remove duplicates

    # If no explicit 'Skills' section, use keyword matching
    else:
        # Define a comprehensive list of keywords for skills
        skills_keywords = ['Python', 'Java', 'C++', 'Machine Learning', 'Deep Learning', 'AWS', 'TensorFlow', 'SQL',
                           'JavaScript', 'HTML', 'CSS', 'Docker', 'Kubernetes', 'React', 'Angular', 'R', 'NoSQL',
                           'PostgreSQL', 'Flask', 'Django', 'Scikit-learn', 'Pandas', 'NumPy', 'PyTorch']

        # Find skills by keyword matching
        skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
        return list(set(skills)) if skills else ["No skills found"]

# Example usage
if __name__ == "__main__":
    jd_text = """
    Responsibilities:
    - Design, develop, and maintain Python-based applications.
    - Write clean, efficient, and reusable code.
    
    Skills:
    - Python, Django, Flask, AWS, Docker, Kubernetes
    - JavaScript, React, HTML, CSS

    Qualifications:
    - Bachelor's degree in Computer Science.
    - 2+ years of experience in software development.
    """

    extracted_skills = extract_skills(jd_text)
    print("Extracted Skills:", extracted_skills)
