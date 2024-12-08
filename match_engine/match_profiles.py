import json
import fitz  # PyMuPDF for PDF text extraction
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Initialize SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to extract text from PDF (resume)
def extract_text_from_pdf(pdf_filepath):
    """Extract text from a PDF file."""
    text = ""
    with fitz.open(pdf_filepath) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    return text

def extract_jd_from_txt(jd_filepath):
    """Extract job descriptions from a .txt file."""
    with open(jd_filepath, 'r', encoding='utf-8') as file:
        jd_text = file.read()
    # Split job descriptions based on 5 newlines
    jd_list = jd_text.split("\n\n\n\n\n")
    return jd_list

# Function to calculate cosine similarity between two texts
def calculate_similarity(text1, text2):
    """Calculate cosine similarity between two text embeddings and return as percentage."""
    embeddings1 = model.encode(text1)
    embeddings2 = model.encode(text2)
    
    # Convert embeddings to float for JSON serialization
    embeddings1 = embeddings1.astype(float)
    embeddings2 = embeddings2.astype(float)
    
    similarity = cosine_similarity([embeddings1], [embeddings2])
    
    # Convert cosine similarity to percentage and round to two decimal places
    similarity_percentage = round(similarity[0][0] * 100, 2)
    return similarity_percentage

# Function to process each JD JSON file and compute similarity with the resume
def process_jds_and_store_similarity(jd_dir, resume_text, output_dir, jd_parsed_dir):
    """Process each JD JSON file and compute cosine similarity with the resume."""
    result = {}  # Dictionary to store JD filenames and similarity percentages
    jd_index = 1  # Initialize JD index (jd1, jd2, jd3, ...)
    
    for jd_filename in os.listdir(jd_dir):
        if jd_filename.endswith(".txt"):
            jd_filepath = os.path.join(jd_dir, jd_filename)
            
            # Extract JD data from the text file
            jd_list = extract_jd_from_txt(jd_filepath)
            
            for index, jd_text in enumerate(jd_list):
                # Construct the parsed JD JSON file path
                json_filepath = os.path.join(jd_parsed_dir, f'parsed_jd_{index+1}.json')
                
                # Load the job description JSON file
                if os.path.exists(json_filepath):
                    with open(json_filepath, 'r') as json_file:
                        jd_data = json.load(json_file)
                    
                    # Extract the job role from the JSON data
                    job_role = jd_data.get("job-role", "unknown-role")
                    
                    # Calculate cosine similarity between resume and JD text
                    similarity_percentage = calculate_similarity(resume_text, jd_text)
                    
                    # Store the result for each JD
                    result[f"jd-{index+1} {job_role}"] = similarity_percentage
          
    # Save results to a JSON file
    output_filepath = os.path.join(output_dir, 'jd_similarity_results.json')
    with open(output_filepath, 'w') as output_file:
        json.dump(result, output_file, indent=4)
    
    print(f"Similarity results stored in: {output_filepath}")

# Main function
def main():
    resume_pdf_filepath = '../inputs/Maunik_Vaghani_Res.pdf'  # Path to the resume PDF
    jd_dir = '../inputs'  # Directory containing JD text files
    output_dir = '../outputs/jd_similarity'  # Directory to store the similarity results
    jd_parsed_dir = '../outputs'  # Directory containing parsed JD JSON files
    
    # Extract text from the resume PDF
    resume_text = extract_text_from_pdf(resume_pdf_filepath)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process all JDs and store similarity results
    process_jds_and_store_similarity(jd_dir, resume_text, output_dir, jd_parsed_dir)

# Run the main function
if __name__ == "__main__":
    main()
