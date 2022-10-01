import os

# Plain text to morse code dictionary.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}

# Morse code to plain text dictionary.
REV_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def translate(text):
    if not all(t == '.' or t == '-' or t == '/' or t.isspace() for t in text):
        print()
        print("The morse code encryption of the text is :-")
        print()
        return ' '.join([MORSE_CODE_DICT.get(t, '?') for t in text])
    else:
        print()
        print("The translated text is :-")
        print()
        return ''.join([REV_MORSE_CODE_DICT.get(t, '?')
                        for t in text.split()])


if __name__ == "__main__":
    os.system('cls')
    print("-" * 50)
    print("ENTER MORSE CODE SENTENCE TO DECODE AND NORMAL SENTENCE TO ENCODE")
    print("-" * 50)
    quit = False

    while not quit:
        print()
        user_input = input("Enter a sentence: ")
        print(translate(user_input.upper()))
        print()
        q = input(
            "Do you want another translation ? (Y/Yes) or (N/No): "
        ).lower()
        if q == 'n' or q == 'no':
            quit = True

# Script by Swaraj Baral (github.com/SwarajBaral)
