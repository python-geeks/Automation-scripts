"""
___________________________________________________________________________________________________________________________________________________
|                                                                                                                                                 |
|   To use this script, please check the README.md file in the directory. A quick start to get the project running is described here.             |
|                                                                                                                                                 |
|   1. Create a Groq account and get your API key at https://console.groq.com/login.                                                              |
|                                                                                                                                                 |
|   2. Either:                                                                                                                                    |
|      - Add your API key directly to line 38: API_KEY = "your_groq_api_key_here", or                                                             |
|      - Create a .env file in the same directory, and add GROQ_API_KEY=your_groq_api_key_here.                                                   |
|                                                                                                                                                 |
|   3. Place all your PDFs in a folder named ''Source'' in the same directory as this script.                                                      |
|                                                                                                                                                 |
|   4. Run the script:                                                                                                                            |
|      python quiz_generator.py                                                                                                                   |
|                                                                                                                                                 |
|   The generated MCQ quiz will be saved in a file called 'generated_mcq_quiz.txt'.                                                               |
|_________________________________________________________________________________________________________________________________________________|
"""


# Change this if you want to set the number of MCQ's
num_questions = 5



import os
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter


load_dotenv(find_dotenv())
API_KEY = os.environ["GROQ_API_KEY"]


def extract_text_from_pdfs():
    print(f"Extracting text from PDF files in the folder: '{'Source'}'...")
    all_text = []
    for file_name in os.listdir('Source'):
        if file_name.endswith(".pdf"):
            file_path = os.path.join('Source', file_name)
            print(f"Processing file: {file_name}")
            reader = PdfReader(file_path)
            for page in reader.pages:
                all_text.append(page.extract_text())
    print("Text extraction completed.")
    return " ".join(all_text)



def generate_unique_mcq(text, num_questions=5):
    print(f"Splitting text into chunks and creating embeddings for LLM processing...")
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0
    )
    docs = text_splitter.create_documents([text])

    embeddings = HuggingFaceEmbeddings()
    store = FAISS.from_documents(docs, embeddings)

    print(f"Connecting to LLM to generate {num_questions} unique MCQs...")
    llm = ChatGroq(
        temperature=0.2,
        model="llama-3.1-70b-versatile",
        api_key=API_KEY
    )

    retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=store.as_retriever()
    )

    quiz = []
    query = f"Generate {num_questions} unique multiple choice questions from the following text: {text} " \
            f"Provide 4 answer options and also the correct answer in plaintext."
    
    response = retrieval_chain.invoke(query)
    question_and_options = response['result']
    quiz.append(question_and_options)

    print("MCQ generation completed.")
    return quiz



def save_mcq_to_file(quiz, file_name="generated_mcq_quiz.txt"):
    output_folder = "Generated_Quizes"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Folder '{output_folder}' created.")
    
    file_path = os.path.join(output_folder, file_name)
    
    print(f"Saving the generated MCQs to file: '{file_path}'...")
    with open(file_path, "w") as f:
        for i, question in enumerate(quiz, 1):
            f.write(f"Question {i}:\n{question}\n\n")
    
    print(f"MCQ Quiz saved to {file_path}")



if __name__ == "__main__":
    if not os.path.exists('Source'):
        print(f"Folder '{'Source'}' not found.")
    else:
        print(f"Folder '{'Source'}' found. Starting process...")
        text = extract_text_from_pdfs()
        print("Text extracted from PDFs.")
        
        mcq_quiz = generate_unique_mcq(text, num_questions=num_questions)
        save_mcq_to_file(mcq_quiz)
        print("Process completed successfully.")
