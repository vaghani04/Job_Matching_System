import re

def extract_technologies(text):
    """Extract the technologies from the job description text."""
    # Define a simple pattern for matching technology-related keywords
    technologies_keywords = ['AWS', 'Azure', 'Docker', 'Kubernetes', 'SQL', 'MongoDB', 'React', 'Angular', 'Node.js', 'Python', 'Java', 'C++', 'JavaScript']
    
    # Find technologies by matching with the keywords
    technologies = []
    for tech in technologies_keywords:
        if tech.lower() in text.lower():
            technologies.append(tech)

    return technologies if technologies else ["No technologies found"]
