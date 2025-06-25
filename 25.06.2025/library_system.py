# Filename:  library_system.py
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"

library = []
library.append(Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0618002255"))
library.append(Book("Pride and Prejudice", "Jane Austen", "978-0141439518"))


def check_out(library, isbn):
    for book in library:
        if book.isbn == isbn and book.available:
            book.available = False
            print(f"Book '{book.title}' checked out successfully.")
            return
    print("Book not found or already checked out.")

check_out(library, "978-0141439518")

for book in library:
    print(book)