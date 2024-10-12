Language Detection Tool
# Language Detection Tool

This is a simple Python tool that detects the language of the input text using the `langdetect` library. You can enter any text in any language, and the program will automatically detect and display the language code.

## Features

- Detects the language of any given text input.
- Supports multiple languages.
- Simple and easy to use.

## Prerequisites

Before running the project, you need to have Python installed on your machine. Additionally, you need to install the `langdetect` library.

## Installation

## Installation

To install the required library, you can use the following command:

```bash
pip install langdetect
```

Alternatively, you can install it from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

```python
from langdetect import detect

text = "Your text here"
language = detect(text)
print(f"The detected language is: {language}")
```

## License

This project is licensed under the MIT License.