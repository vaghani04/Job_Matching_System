import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Initialize SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the job description (JD) and resume data
def load_json_data(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

# Extract data from the JD and resume (generic function)
def extract_data(data, key):
    """Extract specific data (e.g., skills, experience, education) from the JD or resume."""
    return [item for item in data.get(key, [])]

# Function to calculate cosine similarity between two sets of text (skills, experience, education, technology)
def calculate_similarity(text1, text2):
    """Calculate cosine similarity between two text embeddings and return as percentage."""
    embeddings1 = model.encode(text1)
    embeddings2 = model.encode(text2)
    similarity = cosine_similarity([embeddings1], [embeddings2])
    
    # Convert cosine similarity to percentage and round to two decimal places
    similarity_percentage = round(similarity[0][0] * 100, 2)
    return similarity_percentage

# Function to process each JD and store the similarity in a JSON file
def process_jds_and_store_similarity(jd_dir, resume_filepath, output_dir):
    """Process each JD file and compute similarities with the resume."""
    # Load resume data
    resume_data = load_json_data(resume_filepath)

    # Extract relevant sections from the resume
    resume_skills = " ".join(extract_data(resume_data, 'skills'))
    resume_experience = " ".join(extract_data(resume_data, 'experience'))
    resume_education = " ".join(extract_data(resume_data, 'education'))
    resume_technologies = " ".join(extract_data(resume_data, 'technologies'))

    # Loop through all JD files in the directory
    for jd_filename in os.listdir(jd_dir):
        if jd_filename == 'resume_text.json':
            continue
        if jd_filename.endswith(".json"):
            jd_filepath = os.path.join(jd_dir, jd_filename)
            jd_data = load_json_data(jd_filepath)

            # Extract relevant sections from the JD
            jd_skills = " ".join(extract_data(jd_data, 'skills'))
            jd_experience = " ".join(extract_data(jd_data, 'experience'))
            jd_education = " ".join(extract_data(jd_data, 'education'))
            jd_technologies = " ".join(extract_data(jd_data, 'technologies'))

            # Calculate cosine similarity for each section and convert to percentage
            skill_similarity = calculate_similarity(jd_skills, resume_skills)
            experience_similarity = calculate_similarity(jd_experience, resume_experience)
            education_similarity = calculate_similarity(jd_education, resume_education)
            technology_similarity = calculate_similarity(jd_technologies, resume_technologies)

            # Prepare result and save it to the JD file
            result = {
                "jd_filename": jd_filename,
                "skills_similarity": float(skill_similarity),  # Convert to native float
                "experience_similarity": float(experience_similarity),  # Convert to native float
                "education_similarity": float(education_similarity),  # Convert to native float
                "technology_similarity": float(technology_similarity)  # Convert to native float
            }

            output_filename = f"{jd_filename.replace('.json', '')}_similarity.json"
            output_filepath = os.path.join(output_dir, output_filename)

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            with open(output_filepath, 'w') as output_file:
                json.dump(result, output_file, indent=4)

            print(f"Processed {jd_filename} and stored similarity in {output_filename}")

# Main function to initiate the processing
def main():
    jd_dir = '../outputs'  # Directory containing JD JSON files
    resume_filepath = '../outputs/resume_text.json'  # Path to the resume JSON file
    output_dir = '../outputs/jd_similarity'  # Directory to store the output similarity results
    
    # Process all JDs and store results
    process_jds_and_store_similarity(jd_dir, resume_filepath, output_dir)

# Run the main function
if __name__ == "__main__":
    main()
