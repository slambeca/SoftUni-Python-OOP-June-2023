from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormater(ABC):
    @abstractmethod
    def format(self, book: Book):
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class PaperFormatter(BaseFormater):
    def format(self, book: Book) -> str:
        return book.content


class WebFormatter(BaseFormater):
    def format(self, book: Book):
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class Printer:
    def __init__(self, formater: BaseFormater):
        self.formater = formater

    def get_book(self, book: Book):
        return self.formater.format(book)


book = Book("a", "a", "content")
pa = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(pa.get_book(book))
print(pb.get_book(book))