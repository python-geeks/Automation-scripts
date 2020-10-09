#  Title :- Spell Corrector
#  The Spell Corrector is an application which takes text input from the user and corrects spelling errors in it

from textblob import TextBlob
import sys

# Function for correcting spelling errors


def spell_correct(text):
    spell = TextBlob(text)
    # Using TextBlob.correct() method to correct spelling errors
    after_correction = spell.correct()
    return after_correction

# Takes text input from user and call the spell_correct() function


def main():
    after_correction = ""
    for text in map(spell_correct, sys.argv[1:]):
        after_correction += str(text) + ' '
    print(after_correction)

# Running the main() function


if __name__ == '__main__':

    main()
