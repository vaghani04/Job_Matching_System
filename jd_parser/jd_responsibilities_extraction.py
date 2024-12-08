import re

def extract_responsibilities(text):
    """Extract the responsibilities section from the job description text."""
    # Define a simple pattern to capture everything after 'Responsibilities' until a new section starts
    responsibilities_pattern = re.compile(
        r'(?<=\bRESPONSIBILITIES\b[:\-]?\s*)(.*?)(?=\n{2,}|\b(Skills|Qualifications|Technologies)\b|\Z)',
        re.DOTALL | re.IGNORECASE
    )
    
    match = responsibilities_pattern.search(text)
    
    if match:
        # Extract and clean up the responsibilities text
        responsibilities_text = match.group(1).strip()
        # Split by lines and clean up the responsibilities list
        responsibilities = [resp.strip('- ').strip() for resp in responsibilities_text.split('\n') if resp.strip()]
        return responsibilities if responsibilities else ["No responsibilities listed"]
    else:
        return ["No responsibilities listed"]