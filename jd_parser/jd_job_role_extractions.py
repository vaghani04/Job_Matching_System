import re

def extract_job_role(text):
    """Extract job role from the job description text."""
    # Use regex to dynamically identify the 'Job-Role' section in the JD
    job_role_section_pattern = re.compile(
        r'(JOB-ROLE|ROLE)(.*?)(?=RESPONSIBILITIES|SKILLS|QUALIFICATIONS|TECHNOLOGIES|$)', 
        re.DOTALL | re.IGNORECASE
    )
    job_role_section = job_role_section_pattern.search(text)
    
    # If a 'Job-Role' section is found, process it
    if job_role_section:
        job_role_text = job_role_section.group(2)
        # Clean the extracted text
        job_role_text = re.sub(r'[\n\r]', ' ', job_role_text)  # Replace newlines with spaces
        job_role_text = re.sub(r'[:\-]', '', job_role_text)  # Remove unwanted symbols like colon and hyphen
        job_role_text = job_role_text.strip()  # Trim leading/trailing spaces

        return job_role_text

    return "Job role not found"