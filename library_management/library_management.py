# library_management.py

library_records = []


def add_book(title, author, year):
    book = {
        "title": title, "author": author, "year": year, "status": "available"
    }
    library_records.append(book)
    print(f'Book "{title}" added successfully!')


def delete_book(title):
    global library_records
    library_records = [
        book for book in library_records if book["title"] != title
    ]
    print(f'Book "{title}" deleted successfully!')


def checkout_book(title):
    for book in library_records:
        if book["title"] == title and book["status"] == "available":
            book["status"] = "checked out"
            print(f'You have checked out "{title}".')
            return
    print(f'Book "{title}" is not available.')


def return_book(title):
    for book in library_records:
        if book["title"] == title and book["status"] == "checked out":
            book["status"] = "available"
            print(f'You have returned "{title}".')
            return
    print(f'Book "{title}" is not checked out.')


def display_books():
    print("Library Records:")
    for book in library_records:
        print(f'Title: {book["title"]}, Author: {book["author"]}, '
              f'Year: {book["year"]}, Status: {book["status"]}')


if __name__ == "__main__":
    add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    display_books()
    checkout_book("The Great Gatsby")
    display_books()
    return_book("The Great Gatsby")
    display_books()
    delete_book("To Kill a Mockingbird")
    display_books()
