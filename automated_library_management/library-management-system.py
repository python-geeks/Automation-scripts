# A basic program for library management

class Library:
    def __init__(self ,bookList , accountdetails):
        self.bookList = bookList
        self.accountdetails = accountdetails

    def libraryStatus(self):
        finalList = "\n".join(self.bookList)
        print(f"\nAvalaible books for now are as follows-")
        print("\n" , finalList)   

    def bookReturn(self , bookName):
        self.bookList.append(bookName)
        print(f"Thanks for returning or donating {bookName}, have a good day")

    def borrowBook(self , bookName1):
        if bookName1 in self.bookList:
            self.bookList.remove(bookName1)
            print(f"\nYou have been issued {bookName1} , please return it in 30 days .")
            return True
        else:
            print(f"Sorry , {bookName1} is not available for now.")    
            return False

    def policy(self):
        print(f"""----------POLICIES----------
        1) The book issued should be returned in 30 days from the date of issueing.
        2) Charges are applied to the late returner.
        3) Keep scilence while you are in the library.
        4) You are not allowed to use foul language in the library .""")  

    def accountOpen(self , studentName , bookName2):
        if bookName2 in self.bookList:
            self.bookList.remove(bookName2)
            b = {(studentName) : (bookName2) }
            self.accountdetails.update(b)
            print(f"Your account has been opened successfully.")
        else:
            print(f"Sorry {bookName2} is not available for now.")    

    def getDetails(self):
        print(f"People with the book they ever borrowed(member of this library):\n{self.accountdetails}")

class Student:
    def studentName(self):
        self.name = input("Please enter your name: ")
        return self.name

    def requestBook(self):
        self.book = input("\nPlease enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("\nPlease enter the name of the book you want to return or donate: ")
        return self.book



if __name__ == "__main__":
    dakshLibrary = Library(["Harry Potter" , "Physics and Matter" , "Black Hole" , "Python" , "HC V" , "Do Epic Shit"] , {"Rohan" : "Words" , "Shubham" : "Scilence" , "Shibu" : "Time Travel"})       
    student = Student()     
    while(True):
        welcomemsg = '''\n ====== Welcome to People's Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return/Donate a book
        4. Account Opening 
        5. Accout Details
        6. Policies of the Library
        7. Exit the Library
        '''
        print (welcomemsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            dakshLibrary.libraryStatus()

        elif a == 2:
            dakshLibrary.borrowBook(student.requestBook())   

        elif a == 3:
            dakshLibrary.bookReturn(student.returnBook())     

        elif a == 4:
            dakshLibrary.accountOpen(student.studentName(), student.requestBook())    

        elif a == 5:
            dakshLibrary.getDetails()

        elif a == 6:
            dakshLibrary.policy()

        elif a == 7:
            print(f"\nThanks for choosing People's Library , visit again")
            exit()    

        else:
            print(f"Invalid choice , please enter a choice from the given data.")    
