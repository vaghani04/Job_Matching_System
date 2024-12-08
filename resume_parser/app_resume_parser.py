import json
from name_extraction import extract_name
from skills_extraction import extract_skills
from experience_extraction import extract_experience
from education_extraction import extract_education
from contact_info_extraction import extract_contact_info
from text_processing import clean_text, remove_bullets
from project_extraction import extract_projects
from certifications_extraction import extract_certifications
from technology_extraction import extract_tools_technologies
import os

def parse_resume(resume_text, output_filename):
    """Main function to parse resume text and extract structured information."""
    # Extract different sections from the resume
    text = remove_bullets(resume_text)
    text = clean_text(text)
    name = extract_name(text)
    contact_info = extract_contact_info(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)
    project = extract_projects(text)
    certificates = extract_certifications(text)
    technologies = extract_tools_technologies(text)

    # Prepare the structured data
    parsed_data = {
        # "name": name,
        "contact_info": contact_info,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": project,
        # "certificates": certificates
        "technologies": technologies
    }

    # Store the parsed data in a JSON file in the output directory
    output_dir = "..\outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w') as output_file:
        json.dump(parsed_data, output_file, indent=4)
    
    print(f"Resume data has been saved to {output_path}")
