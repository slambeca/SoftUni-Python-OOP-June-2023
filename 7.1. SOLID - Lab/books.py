class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def turn_page(self, page):
        self.current_page = page

    def next_page(self):
        self.current_page += 1


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [b for b in self.books if b.title == title]
        except IndexError:
            return "Book does not exist"


b1 = Book("Test1", "T", 100)
b2 = Book("Test2", "T", 200)
b3 = Book("Test3", "T", 300)
b4 = Book("Test4", "T", 400)

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

print(library.find_book("Test1"))