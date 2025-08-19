import unittest
from flashcards import Flashcards

class TestGuesser(unittest.TestCase):
    # the test cards have two categories
    # Pacman: {Pacman: "the player character in the game PacMan"}
    # Spanish: {}
    def setUp(self):
        self.flashLib = Flashcards()
        self.flashLib.add_category("Pacman")
        self.flashLib.add_card("Pacman","Pacman","the player character in the game PacMan")
        self.flashLib.add_category("Spanish")
    
    # tests that new categories can be added and that existing categories cannot be added
    def testAddCategories(self):
        self.assertTrue(self.flashLib.add_category("Japanese")) # the category Japanese does not exist, and can be added
        self.assertFalse(self.flashLib.add_category("Pacman")) # the category Pacman exists, so cannot be added again

    # tests that new cards can be added to an existing category, but not to one that does not exist
    def testAddCards(self):
        self.assertTrue(self.flashLib.add_card("Pacman","Inky","the blue ghost in the game PacMan"))
        self.assertFalse(self.flashLib.add_card("Nonexistant","Blinky","the red ghost in the game PacMan"))
    
        # self.assertTrue(self.flashLib.add_card("Pacman","Clyde","the orange ghost in the game PacMan"))
        # self.assertTrue(self.flashLib.add_card("Pacman","Clyde","the loser ghost in the game PacMan")) input: 'y'
        # self.assertFalse(self.flashLib.add_card("Pacman","Clyde","the orange ghost in the game PacMan")) input: 'n'
        # self.assertFalse(self.flashLib.add_card("Pacman","Clyde","the orange ghost in the game PacMan")) input: anything else

    # tests that existing categories can be deleted and that nonexisting categories cannot
    def testDeleteCategories(self):
        self.assertTrue(self.flashLib.add_category("Test"))
        self.assertTrue(self.flashLib.add_card("Test","front","back"))
        self.assertTrue(self.flashLib.delete_category("Test"))
        self.assertFalse(self.flashLib.delete_category("Test"))

    # tests that existing cards can be deleted and that nonexisting cards and cards from nonexisting categories cannot
    def testDeleteCards(self):
        self.assertTrue(self.flashLib.add_category("Test"))
        self.assertTrue(self.flashLib.add_card("Test","front","back"))
        self.assertFalse(self.flashLib.delete_card("Test","back"))
        self.assertTrue(self.flashLib.delete_card("Test","front"))
        self.assertFalse(self.flashLib.delete_card("Test","front"))
        self.assertFalse(self.flashLib.delete_card("Nonexistant", "front"))

    # tests that save and load works
    def testSaveAndLoad(self):
        testCards = Flashcards()
        testCards.add_category("Test")
        testCards.add_card("Test","front","back")
        #testCards.save()
        
        newCards = Flashcards()
        newCards.load()

        self.assertFalse(newCards.add_category("Test"))

    # tests that review works correctly
    def testReview(self):
        self.assertFalse(self.flashLib.review("Spanish"))
        # self.assertTrue(self.flashLib.review("Pacman"))

if __name__ == '__main__':
    unittest.main()
