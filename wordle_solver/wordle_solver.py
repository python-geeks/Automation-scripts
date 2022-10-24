# https://github.com/dwyl/english-words for the list of words

from audioop import add
from operator import contains
from re import L
import string
from typing import Set
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pynput import keyboard
import time


def on_release(key):
    # Start button
    if key == keyboard.Key.esc:
        return False  # stop listener


def get_row_results(game_row):
    tiles = game_row.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
    evaluation = []
    eval_to_int = {
        "correct": 1,
        "present": 0,
        "absent": -1,
        "empty": -2,
        "tbd": -3
    }
    for tile in tiles:
        evaluation.append(eval_to_int[tile.get_attribute("data-state")])
    print(evaluation)

    return tuple(evaluation)


def enter_word(word):
    keyboard_controller = keyboard.Controller()
    keyboard_controller.type(word)
    keyboard_controller.tap(keyboard.Key.enter)
    time.sleep(2)


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


# From the basic list of words, return all the words with 5 characters.
def get_list_of_words():
    list_of_words = open("words_alpha.txt", "r").read().strip().splitlines()
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
def solving_algorithm(word, res):
    print("solving_algorithm start")

    list_of_words = get_list_of_words()
    absent_letters = set([])
    present_letters = set([])

    solution = "tbest"  # developpement solution
    solving_string = "*****"

    for letter in range(len(word)):
        print("letter : ", word[letter])
        if res[letter] == 1:  # Case when the status of the letter is "correct"
            print("letters in the right position : ", solution[letter])
            print("GREATOOOOO")
            solving_string = solving_string[:letter] + word[letter] + solving_string[letter + 1:]
        elif res[letter] == 0:  # status is present
            print("the letter is present")
            solving_string = solving_string[:letter] + "_" + solving_string[letter + 1:]
            present_letters.add(word[letter])
        else:  # status is absent
            print("the letter is absent")
            absent_letters.add(word[letter])  # Case when the status of the letter is 'absent'
            solving_string = solving_string[:letter] + "*" + solving_string[letter + 1:]

    print("Update list of word")
    print("length of list", len(list_of_words))

    # Update list of words
    buffer_list = []

    for absent in absent_letters:
        print(absent)
        list_of_words = list(filter(check_letter_in_word(absent, list_of_words), list_of_words))

    list_of_words = buffer_list



    print("letter not in the right position : ", present_letters)
    print("Letters with absent status", absent_letters)
    print("solving string :", solving_string)
    # print(list_of_words)
    print("lenght of list", len(buffer_list))


def main():
    # Start the browser
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.get("https://www.nytimes.com/games/wordle/index.html")

    # Wait for start
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
    print("Starting")

    # Get the game rows
    game_rows = browser.find_elements(By.CLASS_NAME, 'Row-module_row__dEHfN')

    first_string = "tests"
    enter_word(first_string)
    res = get_row_results(game_rows[0])
    solving_algorithm(first_string, res)

    time.sleep(1)

    second_string = "trees"
    enter_word(second_string)
    get_row_results(game_rows[1])


if __name__ == "__main__":
    main()
