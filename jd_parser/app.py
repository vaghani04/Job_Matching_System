import os
import json
from app_jd_parser import parse_job_description

def split_job_descriptions(file_path):
    """
    Splits a file containing multiple job descriptions into individual JDs.
    A new JD starts where there are at least 5 consecutive newline characters.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split based on 5 or more consecutive newline characters
    job_descriptions = [jd.strip() for jd in content.split('\n\n\n\n\n') if jd.strip()]
    return job_descriptions

def save_parsed_jd(output_dir, jd_data, index):
    """
    Saves parsed JD data to a JSON file in the output directory.
    """
    file_name = f"parsed_jd_{index + 1}.json"
    output_path = os.path.join(output_dir, file_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(jd_data, f, indent=4)
    print(f"Saved parsed JD to {output_path}")

def main():
    # Input and output directories
    input_file = '../inputs/job_descriptions.txt'
    output_dir = '../outputs/'

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Split job descriptions
    job_descriptions = split_job_descriptions(input_file)
    print(f"Found {len(job_descriptions)} job descriptions to parse.")

    # Step 2: Parse and save each JD
    for index, jd_text in enumerate(job_descriptions):
        parsed_data = parse_job_description(jd_text)
        save_parsed_jd(output_dir, parsed_data, index)

if __name__ == "__main__":
    main()
