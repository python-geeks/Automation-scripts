# https://www.wordunscrambler.net/word-list/wordle-word-list
# for the list of words

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pynput import keyboard
import time


# This class is used to store data about the wordle such as :
# - the list of possible words
# - the letters that are present but not in the right position
# - the letters that are absent
# - the letters that are correct and their position in a list
# - the word that is currently being tested

class Finder:
    def __init__(self):
        self.possible_words = get_list_of_words()
        self.present_letters = set([])
        self.absent_letters = set([])
        self.word = [''] * 5

        # Creators recommend “Slate” as starting word
        self.word_to_try = "slate"


# Function that is called by the KeyboardListener
def on_release(key):
    # Start button
    if key == keyboard.Key.esc:
        return False  # stop listener


# Get the status of the letters in the wordle
def get_row_results(game_row):
    tiles = game_row.find_elements(
        By.XPATH, ".//*[contains(@class, 'Tile-module_tile__')]")
    row_results = []
    res_to_int = {
        "correct": 1,
        "present": 0,
        "absent": -1,
        "empty": -2,
        "tbd": -3
    }
    for tile in tiles:
        row_results.append(res_to_int[tile.get_attribute("data-state")])
    print(f"Row results : {row_results}")

    return tuple(row_results)


# Enter the word in the wordle
def enter_word(word):
    keyboard_controller = keyboard.Controller()
    keyboard_controller.type(word)
    keyboard_controller.tap(keyboard.Key.enter)
    time.sleep(2)


# Check word length, used in get_list_of_words()
# if the source list contains words with different length
def check_word_length(word):
    if len(word) != 5:
        return False
    else:
        return True


# Check if a word contains a specific letter
def check_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


# Check if the letter in the finder object
# is the same as the letter in the possible answer
def check_match(finder_word_letter, possible_word_letter):
    if finder_word_letter == possible_word_letter:
        return True
    else:
        return False


# From the wordle words list, return all the words
def get_list_of_words():
    list_of_words = open("words_alpha.txt", "r").read().strip().splitlines()

    # *** Use this if the source list contains words with different length ***
    # list_of_words = list(filter(check_word_length, list_of_words))

    return list_of_words


# Algorithm that solve the wordle
def solving_algorithm(res, finder):
    print("Starting solving algorithm")
    word = finder.word_to_try

    # Compare the word with the results of the wordle
    for letter in range(len(word)):
        # Case when the status of the letter is "correct"
        if res[letter] == 1:
            print(f"Letter {word[letter]} is correct")
            finder.word[letter] = word[letter]
            print(finder.word)
            if word[letter] in finder.absent_letters:
                finder.absent_letters.remove(word[letter])

        # Case when the status of the letter is "present"
        # (present but at the wrong position)
        elif res[letter] == 0:
            print(f"Letter {word[letter]} is present")
            finder.present_letters.add(word[letter])
            # We keep all the words that don't match
            # the pattern of the word entered
            finder.possible_words = list(
                filter(lambda x_word:
                       not check_match(word[letter], x_word[letter]),
                       finder.possible_words))

        else:  # Case when the status of the letter is "absent"
            print(f"Letter {word[letter]} is absent")
            if word[letter] not in finder.present_letters:
                finder.absent_letters.add(word[letter])

            # We keep all the words that don't match
            # the pattern of the word entered
            finder.possible_words = list(
                filter(lambda x_word:
                       not check_match(word[letter], x_word[letter]),
                       finder.possible_words))

    print("\n")
    print("Updating list of possible words ...")

    # Update list of words
    for absent in finder.absent_letters:
        finder.possible_words = list(
            filter(lambda x_word:
                   not check_letter_in_word(absent, x_word),
                   finder.possible_words))
    for present in finder.present_letters:
        finder.possible_words = list(
            filter(lambda x_word:
                   check_letter_in_word(present, x_word),
                   finder.possible_words))
    for i in range(len(finder.word)):
        if finder.word[i] != "":
            finder.possible_words = list(
                filter(lambda x_word:
                       check_match(x_word[i], finder.word[i]),
                       finder.possible_words))

    # Update the next word to try
    finder.word_to_try = finder.possible_words[0]

    print("List of possible words updated !\n")

    print("Letter not in the right position : ", finder.present_letters)
    print("Letters with absent status : ", finder.absent_letters)
    print("List of words : ", finder.possible_words)
    print("Length of list", len(finder.possible_words))


def main():
    # Start the browser
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    browser.get("https://www.nytimes.com/games/wordle/index.html")

    # Create the finder object (cf. class Finder)
    finder = Finder()

    guesses_left = 6

    # Wait for start
    with keyboard.Listener(on_release=on_release, suppress=True) as listener:
        print("Starting program\n")
        listener.join()

    # With "suppress=True", duplicate key presses are not sent
    # to the application but for some reason I need to add a delay
    # for the first input to be sent.
    time.sleep(1)

    # Get the game rows
    game_rows = browser.find_elements(
        By.XPATH, "//*[contains(@class, 'Row-module_row__')]")

    # Enter words until the game is over or the wordle is solved
    for i in range(guesses_left, 0, -1):
        enter_word(finder.word_to_try)
        res = get_row_results(game_rows[guesses_left - i])
        solving_algorithm(res, finder)
        if len(finder.possible_words) == 1:
            enter_word(finder.word_to_try)
            print(f"The word is : {finder.word_to_try}\n")
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
