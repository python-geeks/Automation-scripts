from tkinter import *
from flashcards import Flashcards

# the class for the Flashcards Application, using tkinter
# note: unfinished, also my first time using tkinter
# things to add:
#   back button
#   delete categories/cards feature
#   review/quiz features
#       use click event functions
#   finish add categories/cards
#       when a category is added or selected, should take user to add cards scene
class FlashcardsUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Flashcard App")
        
        self.frame = Frame(self.root, width=300, height=250)
        #self.frame.bind("<Button-1>", self.leftClick)
        #self.frame.bind("<Button-2>", self.middleClick)
        #self.frame.bind("<Button-3>", self.rightClick)
        self.frame.pack()

        self.flashcards = Flashcards()
        self.flashcards.load()
        
        self.home()

        self.root.mainloop()
    
    # homescreen, with the options to add cards, review, or quiz
    def home(self):
        label = Label(self.root, text="Flashcards", font=("Arial Bold", 30))
        label.place(x=50,y=30)

        add_cards = Button(self.root, text="Add Cards", width=10)
        add_cards.place(x=60,y=100)
        add_cards.config(command=self.addCards)

        review_cards = Button(self.root, text="Review", width=10)
        review_cards.place(x=160,y=100)
        review_cards.config(command=self.reviewCards)

        quiz = Button(self.root, text="Quiz", width=10)
        quiz.place(x=110,y=150)
        quiz.config(command=self.quiz)

    # left click event
    def leftClick(self, event):
        print("left")

    # middle click event
    def middleClick(self, event):
        print("middle")

    # right click event
    def rightClick(self, event):
        print("right")

    # clears the screne for a different part of the application
    # ex: home -> review
    def changeScene(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.frame = Frame(self.root, width=300, height=250)
        self.frame.pack()

    # a screen to choose a category, which will then move to adding cards
    # currently only the screen to choose a category is done, and buttons are not functional
    # has a type in bar to create a new category and a scrollbar with existing categories
    def addCards(self):
        self.changeScene()

        categories = list(self.flashcards.categories.keys())
        
        label = Label(self.root, text="Create/Choose a Subject", font=("Arial Bold", 15))
        label.place(x=35,y=30)

        txt = Entry(self.root, width=20, textvariable=StringVar(self.root, "Enter new subject"))
        txt.place(x=90,y=70)

        add = Button(self.root, text="Add Subject", width=20)
        add.place(x=80,y=120)
        add.config(command=self.addCategory(txt.get()))

        add_cards = Button(self.root, text="Choose Subject", width=20)
        add_cards.place(x=80,y=170)
        
        scrollbar = Scrollbar(self.root)
        scrollbar.pack( side = RIGHT, fill = Y )

        mylist = Listbox(self.root, yscrollcommand = scrollbar.set )
        for subject in categories:
            mylist.insert(END, str(subject))

        mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = mylist.yview )

    # update flashcard library categories
    def addCategory(self, category):
        self.flashcards.add_category(category)
        #self.flashcards.save()
        #self.flashcards = self.flashcards.load()

    # scene where card review takes place
    # should display menu of categories
    # when category is chosen, review occurs (use click events)
    def reviewCards(self):
        self.changeScene()
        category_menu = OptionMenu(self.root, StringVar(self.root).set("Select a Category"), list(self.flashcards.categories.keys()))
        category_menu.place(x=50,y=30)
    
    # scene where multiple choice or matching quiz takes place
    # should display menu of categories
    # when category is chosen, quiz occurs
    def quiz(self):
        self.changeScene()
    
if __name__ == '__main__':
    ui = FlashcardsUI()
