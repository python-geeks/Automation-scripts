import os
from PyPDF2 import PdfReader
from datetime import datetime
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

load_dotenv(find_dotenv())
API_KEY = os.environ["GROQ_API_KEY"]

# Change this if you want to set the number of MCQs
num_questions = 5


def extract_text_from_pdfs():
    """Extracts text from PDF files in the 'Source' folder."""
    print("Extracting text from PDF files in the folder: 'Source'...")
    all_text = []

    if len(os.listdir('Source')) == 0:
        print("Source Folder Empty!")
        print("Process exiting...")
        exit(0)

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
    """Generates unique multiple choice questions from text."""
    print("LLM processing...")
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
    query = (
        f"Generate {num_questions} unique multiple choice questions"
        "from the text: {text}"
        "Provide 4 answer options and also the correct answer in plaintext."
    )

    response = retrieval_chain.invoke(query)
    question_and_options = response['result']
    quiz.append(question_and_options)

    print("MCQ generation completed.")
    return quiz


def save_mcq_to_file(quiz, file_name="generated_mcq_quiz.txt"):
    """Saves generated MCQs to a text file."""
    output_folder = "Generated_Quizes"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Folder '{output_folder}' created.")

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"generated_mcq_quiz_{current_time}.txt"
    file_path = os.path.join(output_folder, file_name)

    print(f"Saving the generated MCQs to file: '{file_path}'...")
    with open(file_path, "w") as f:
        for i, question in enumerate(quiz, 1):
            f.write(f"Question {i}:\n{question}\n\n")

    print(f"MCQ Quiz saved to {file_path}")


if __name__ == "__main__":
    if not os.path.exists('Source'):
        print("Folder 'Source' not found.")
    else:
        print("Folder 'Source' found. Starting process...")
        text = extract_text_from_pdfs()
        print("Text extracted from PDFs.")

        mcq_quiz = generate_unique_mcq(text, num_questions=num_questions)
        save_mcq_to_file(mcq_quiz)
        print("Process completed successfully.")
