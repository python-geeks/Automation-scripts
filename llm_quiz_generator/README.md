# Automated Quiz Generator from PDF Files

This Python script automates the process of generating Multiple Choice Questions (MCQs) from the content of PDF files stored in a folder. It extracts the text from the PDFs, generates unique questions with four answer options using a language model (LLM), and saves the quiz as a text file.

- **Automatic PDF Text Extraction**: Extracts text from all PDFs in a specified folder.
- **MCQ Generation**: Generates unique multiple choice questions with 4 answer options and identifies the correct answer.
- **Quiz Output**: Saves the quiz in a text format for easy review.

## Setup Instructions

This guide will walk you through the steps to set up and run the Automated Quiz Generator, which converts PDF content into multiple-choice questions (MCQs). You will need to create an account with Groq to get an API key and set up your Python environment before running the script.

### Step 1: Create a Groq Account and Get an API Key (100% free)

1. **Visit Groq's Console**:  
   Open your web browser and go to [Groq Console](https://console.groq.com/login).

2. **Log In or Create an Account**:  
   You can log in with your email, GitHub account, or create a new Groq account for free.

3. **Generate an API Key**:  
   - After logging in, navigate to the "API Keys" section in the Groq console.
   - Click the "Create API Key" button.
   - Enter a name for your API key (e.g., `quiz_key`).
   - **Important**: After you create the key, Groq will display it **only once**. Be sure to copy it correctly at this time.

4. **Save the API Key**:  
   You will need this key to run the quiz generator script.

---

### Step 2: Add Your API Key to the Script

You have two options to use your API key. We recommend using option 1 since storing API keys directly in your code is risky because it exposes sensitive information, especially if you share or push your code to platforms like GitHub. Using a `.env` file is a safer approach because it keeps your keys private and separate from the code. It also prevents accidental exposure by ensuring the keys aren't included in version control systems like Git. This method enhances security and protects your application from unauthorized access.

#### Option 1: Store the API Key in a `.env` File

1. Create a new file in the same directory as your script and name it `.env`.
2. Open the `.env` file in a text editor.
3. Add the following line to the `.env` file, replacing `your_groq_api_key_here` with your actual API key:
```
GROQ_API_KEY="your_groq_api_key_here"
```
4. Save the `.env` file.

#### Option 2: Paste the API Key Directly into the Script

1. Open the `main.py` file in your code editor.
2. Find the following line in the script (around line 38):
 ```python
 API_KEY = os.environ["GROQ_API_KEY"]
 ```
3. Replace the above line with your API key directly, like this:
 ```python
 API_KEY = "your_groq_api_key_here"
 ```

---

### Step 3: Prepare the PDF Files

1. Create a folder (if not present) called `Source` in the same directory as your Python script.
2. Place all the PDF files that you want to generate quizzes from inside the `Source` folder.

---

### Step 4: Install the Dependencies

1. Install all the required modules using this command:
```
pip install -r requirements.txt
```

---

### Step 5: Run the Script

1. To generate the quiz, open a terminal or command prompt in the folder where the script is located and run the following command:
```
python main.py
```
This will extract the text from the PDFs, generate multiple-choice questions (MCQs) using the language model, and save the output in a folder named `Generated_Quizes`.

---

## Output

The generated MCQ quiz will be saved in a text file with a timestamp in the `Generated_Quizes` folder. Each question will have four options, and the correct answer will be indicated.

## Author(s)

[Naman Verma](https://github.com/NamanVer02/)

## Disclaimers

Please note that the free tier of Groq API has rate limits, which may cause errors if too many requests are made in a short period of time. If you encounter a rate limit error, try reducing the number of PDFs in the 'Source' folder or lower the number of questions being generated. This should help avoid hitting the rate limits. For more information on the exact rate limits, please refer to the [Groq API documentation](https://console.groq.com/settings/limits).
