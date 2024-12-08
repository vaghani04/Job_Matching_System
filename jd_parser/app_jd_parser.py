from jd_skills_extraction import extract_skills
from text_processing import clean_text, remove_bullets
from jd_technology_extraction import extract_technologies
from jd_responsibilities_extraction import extract_responsibilities
from jd_experience_extraction import extract_experience
from jd_qualifications_extraction import extract_qualifications
from jd_job_role_extractions import extract_job_role

def parse_job_description(job_description):
    """Main function to parse job description and extract structured data."""
    # Extract different sections from the job description
    job_description = remove_bullets(job_description)
    job_description = clean_text(job_description)
    skills = extract_skills(job_description)
    qualifications = extract_qualifications(job_description)
    experience = extract_experience(job_description)
    # responsibilities = extract_responsibilities(job_description)
    technologies = extract_technologies(job_description)
    job_role = extract_job_role(job_description)

    return {
        "job-role": job_role,
        "skills": skills,
        "qualifications": qualifications,
        "experience": experience,
        # "responsibilities": responsibilities,
        "technologies": technologies,
    }
