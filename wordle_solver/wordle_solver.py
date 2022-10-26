# https://github.com/dwyl/english-words for the list of words

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pynput import keyboard
import time


class Finder:
    def __init__(self):
        self.possible_words = get_list_of_words()
        self.absent_letters = set([])
        self.present_letters = set([])
        self.word = [''] * 5


def on_release(key):
    # Start button
    if key == keyboard.Key.esc:
        return False  # stop listener


def get_row_results(game_row):
    tiles = game_row.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
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
    print(row_results)

    return tuple(row_results)


def enter_word(word):
    keyboard_controller = keyboard.Controller()
    keyboard_controller.type(word)
    keyboard_controller.tap(keyboard.Key.enter)
    time.sleep(2)


def create_regex(solving_string, present_letters):
    regex = ""
    for letter in range(len(solving_string)):
        if solving_string[letter] == "*":
            regex += "[a-z]"
        elif solving_string[letter] == "_":
            regex += \
                "[^" + str(list(present_letters)).replace("'", "").replace(",", "").replace("[", "").replace(" ", "")
        else:
            regex += "[" + solving_string[letter] + "]"
    return regex


# Check word length
def check_word_length(word):
    if len(word) != 5:
        return False
    else:
        return True


def check_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def check_match(finder_word_letter, possible_word_letter):
    if finder_word_letter == possible_word_letter:
        return True
    else:
        return False


# From the basic list of words, return all the words with 5 characters.
def get_list_of_words():
    # list_of_words = open("words_alpha.txt", "r").read().strip().splitlines()
    list_of_words = open("words_alpha_2.txt", "r").read().strip().splitlines()
    list_of_words = list(filter(check_word_length, list_of_words))

    return list_of_words

    # Print to verify filtered_list only contains 5 characters words.
    # print("list of words : ", list_of_words)


# Algorithm that solve the wordle
# In the string we get :
# _ : the letter is not on the right position (present)
# * : the letter is not in the solution (absent)
# X : the letter is on the right position (correct)
# letters_not_in_response, is a list which keeps track of the allowed letters
# letter_not_in_position, is a list which keeps track of the letters in bad position
# For exemple, "A_A_*A", letters_not_in_response = ['B'], letter_not_in_position = ['K'].
def solving_algorithm(word, res, finder):
    print("solving_algorithm start")

    solving_string = "*****"

    for letter in range(len(word)):
        print("letter : ", word[letter])
        if res[letter] == 1:  # Case when the status of the letter is "correct"
            print("the letter is correct")
            solving_string = solving_string[:letter] + word[letter] + solving_string[letter + 1:]
            finder.word[letter] = word[letter]
            print(finder.word)
        elif res[letter] == 0:  # Case when the status of the letter is "present" (present but at the wrong position)
            print("the letter is present")
            finder.present_letters.add(word[letter])
            solving_string = solving_string[:letter] + "_" + solving_string[letter + 1:]
        else:  # Case when the status of the letter is "absent"
            print("the letter is absent")
            if word[letter] not in finder.present_letters:
                finder.absent_letters.add(word[letter])
                solving_string = solving_string[:letter] + "*" + solving_string[letter + 1:]

    print("Update list of words")
    print("length of list", len(finder.possible_words))

    # Update list of words
    for absent in finder.absent_letters:
        finder.possible_words = list(
            filter(lambda x_word: not check_letter_in_word(absent, x_word), finder.possible_words))
    for present in finder.present_letters:
        finder.possible_words = list(
            filter(lambda x_word: check_letter_in_word(present, x_word), finder.possible_words))
    for i in range(len(finder.word)):
        if finder.word[i] != "":
            finder.possible_words = list(
                filter(lambda x_word: check_match(x_word[i], finder.word[i]), finder.possible_words))

    print("letter not in the right position : ", finder.present_letters)
    print("Letters with absent status", finder.absent_letters)
    print("list of words : ", finder.possible_words)
    print("length of list", len(finder.possible_words))

    regex = create_regex(solving_string, finder.present_letters)  # Create the regex
    print(create_regex(solving_string, finder.present_letters))

    # print("solving string :", solving_string)


def main():
    # Start the browser
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.get("https://www.nytimes.com/games/wordle/index.html")

    finder = Finder()
    guesses_left = 6

    # Wait for start
    with keyboard.Listener(on_release=on_release, suppress=True) as listener:
        print("Starting")
        listener.join()

    # With "suppress=True", duplicate key presses are not sent to the application
    # but for some reason I need to add a delay for the first input to be sent.
    time.sleep(1)

    # Get the game rows
    game_rows = browser.find_elements(By.CLASS_NAME, 'Row-module_row__dEHfN')

    first_string = "slate"
    enter_word(first_string)
    res = get_row_results(game_rows[0])
    solving_algorithm(first_string, res, finder)
    guesses_left -= 1

    time.sleep(1)

    for i in range(guesses_left, 0, -1):
        enter_word(finder.possible_words[0])
        res = get_row_results(game_rows[guesses_left + 1 - i])
        solving_algorithm(finder.possible_words[0], res, finder)
        time.sleep(1)


if __name__ == "__main__":
    main()
