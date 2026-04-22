#Library system
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book issued")
                return
        print("Not available")


lib = Library()
b1 = Book("Python")
b2 = Book("Java")

lib.add_book(b1)
lib.add_book(b2)

lib.issue_book("Python")
lib.issue_book("Python")