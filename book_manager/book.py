
# conn = sqlite3.connect("books.db")

# c = conn.cursor()

# c.execute(""" CREATE TABLE books (
#         name text,
#         path text primary key,
#         tags text,
#         notes text
# )   """)

# c.execute("INSERT INTO books VALUES ('test1', 'path1', 'notes1', 'fiction')")
# conn.commit()


def add_book(conn, book):
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
              (book.name, book.path, book.notes, book.tags))
    conn.commit()


def delete_book(conn, path):
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE path = ? ", (path, ))
    conn.commit()


def edit_book(conn, prop, value, name):
    c = conn.cursor()
    if prop in ['name', 'notes', 'tags', 'path']:
        c.execute(f"UPDATE books SET {prop} = ? WHERE path = ?", (value, name))
        conn.commit()


def show_books(conn):
    c = conn.cursor()
    c.execute("SELECT * from books")
    finresults = []
    results = c.fetchall()
    for i in results:
        finresults.append([i[0], i[1], i[2].split(', '), i[3]])
    return finresults


def search_book(conn, prop, value):
    c = conn.cursor()
    if prop in ['name', 'notes', 'tags', 'path']:
        c.execute(f"SELECT * FROM books where {prop} = ?", (value, ))
        conn.commit()

# print("Welcome to BookMan")
# while True:
#     print("1.Add New Book\n2.Edit a Book\n3.Display all books\n4.Delete a book\n5.Exit")
#     n=int(input())
#     if n==1:
#         name, path, notes, tags= input("Enter Book Details: ").split()
#         add_book(Book(name, path, notes, tags))
#     elif n==2:
#         prop, value, name = input("Enter property, new value and book name: ").split()
#         edit_book(prop, value, name)
#     elif n==3:
#         show_books()
#     elif n==4:
#         name = input("Enter book to delete")
#         delete_book(name)
#     else:
#         break
