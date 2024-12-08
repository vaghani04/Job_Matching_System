import os
import fitz  # PyMuPDF
from app_resume_parser import parse_resume

def extract_text_from_pdf(pdf_path):
    """Extract all text from the given PDF file."""
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Extract text from each page
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        return text
    
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def main():
    """Main function to run the resume parser."""
    # Get the resume file path and output file name from the user
    resume_path = '..\inputs\Maunik_Vaghani_Res.pdf'
    output_filename = 'resume_text.json'

    # Check if the resume is a PDF or text file
    if resume_path.lower().endswith('.pdf'):
        # Extract text from PDF
        print(f"Extracting text from {resume_path}...")
        resume_text = extract_text_from_pdf(resume_path)
        if resume_text is None:
            print("Failed to extract text from the PDF.")
            return
    else:
        # If it's a text file, read the content
        with open(resume_path, "r") as file:
            resume_text = file.read()

    # Call the resume parser function
    print("Parsing resume...")
    parse_resume(resume_text, output_filename)

if __name__ == "__main__":
    main()
