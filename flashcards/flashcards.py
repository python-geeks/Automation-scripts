import pickle
import random

class Flashcards:
    # initializes with an empty dictionary
    # key: category/subject name
    # value: dictionary of cards for the given subject
    #          key: card's front
    #          value: card's back
    def __init__(self):
        self.categories = {}

    # adds a category/subject
    # returns True if subject does not exist and can be added
    # returns False and does not add otherwise
    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = {}
            return True
        else:
            print("Category already exists.")
            return False

    # deletes a category/subject
    # returns True if subject exists and is able to be deleted
    # returns False otherwise
    def delete_category(self, category_name):
        if category_name in self.categories:
            self.categories.pop(category_name)
            return True
        else:
            print("Category does not exist.")
            return False

    # adds a card to a given category
    # if the card exists already, the user is prompted whether or not to override
    # returns True if card is added or overridden
    # returns False otherwise
    def add_card(self, category, front, back):
        if category in self.categories:
            if front in self.categories[category]:
                ans = input("Card exists. Override(y/n)? ")
                if ans == 'y':
                    self.categories[category][front] = back
                    return True
                elif ans == 'n':
                    print("Ok. Exiting.")
                    return False
                else:
                    print("Invalid input. Exiting.")
                    return False
            else: 
                self.categories[category][front] = back
                return True
        else:
            print("Category does not exist.")
            return False

    # deletes a given card from a given category
    # returns True if category and card both exist and deletion completes
    # returns False otherwise
    def delete_card(self, category, front):
        if category in self.categories:
            if front in self.categories[category]:
                self.categories[category].pop(front)
                return True
            else:
                print("Card does not exist.")
                return False
        else:
            print("Category does not exist.")
            return False

    # saves self.categories to a pickle file
    def save(self):
        with open('dict.pickle', 'wb') as f:
            pickle.dump({
                'categories': self.categories
            }, f)

    # loads self.categories from a pickle file
    def load(self):
        with open('dict.pickle', 'rb') as f:
            params = pickle.load(f)
            self.categories = params['categories']

    # shuffles cards in a given category and goes through them
    # after input, the correct answer is shown
    # returns True when review is finished
    # returns False if category does not exist or if the category has no cards
    def review(self, category):
        if category in self.categories and len(self.categories[category]) > 0:
            cards = self.categories[category]
            key_list = list(cards.keys())
            random.shuffle(key_list)
            for card in key_list:
                input(card + ": ")
                print(cards[card])
                print()
            return True
        else:
            print("Category does not exist or is empty.")
            return False

if __name__ == '__main__':
    flashcards = Flashcards()
    flashcards.add_category("Japanese")
    flashcards.add_card("Japanese", "ありがとう", "thank you")
    flashcards.add_card("Japanese", "あめ", "rain")
    flashcards.add_card("Japanese", "あまい", "sweet")
    flashcards.review("Japanese")