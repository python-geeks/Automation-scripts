import re
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


# Function to analyze the structure of the resume
def check_structure(text):
    structure_issues = []
    sections = [
        'Education',
        'Experience',
        'Skills',
        'Certifications',
        'Achievements'
    ]
    for section in sections:
        if section.lower() not in text.lower():
            structure_issues.append(f"Missing section: {section}")
    return structure_issues


# Function to check keyword optimization in the resume
def keyword_optimization(text, keywords):
    text_tokens = word_tokenize(text.lower())
    keywords_found = [word for word in text_tokens if word in keywords]
    return keywords_found


# Function to check for grammar issues
def grammar_check(text):
    grammar_issues = []
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))

    for sentence in sentences:
        words = word_tokenize(sentence)
        filtered_sentence = [w for w in words if not w.lower() in stop_words]
        # Check basic length and punctuation rules
        if len(filtered_sentence) < 3:
            grammar_issues.append(f"Possible fragment: {sentence}")
        if not re.match(r'.*[.!?]$', sentence.strip()):
            grammar_issues.append(f"Missing punctuation: {sentence}")

    return grammar_issues


# Main function to run the resume analyzer
def analyze_resume(pdf_path, keywords):
    text = extract_text_from_pdf(pdf_path)

    print("Analyzing structure...")
    structure_issues = check_structure(text)
    if structure_issues:
        print("Structure Issues Found:")
        for issue in structure_issues:
            print(f"- {issue}")
    else:
        print("Structure looks good.")

    print("\nAnalyzing keyword optimization...")
    found_keywords = keyword_optimization(text, keywords)
    print(f"Keywords found: {', '.join(found_keywords)}")

    print("\nAnalyzing grammar...")
    grammar_issues = grammar_check(text)
    if grammar_issues:
        print("Grammar Issues Found:")
        for issue in grammar_issues:
            print(f"- {issue}")
    else:
        print("No major grammar issues found.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    # Keywords to check for in the resume (can be customized)
    resume_keywords = ['python', 'machine learning', 'data analysis', 'sql']

    # Example usage
    resume_path = 'your_resume.pdf'  # Replace with the actual file path
    analyze_resume(resume_path, resume_keywords)
