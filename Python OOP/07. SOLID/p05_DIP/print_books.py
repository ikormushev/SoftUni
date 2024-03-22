class Book:
    def __init__(self, content: str):
        self.content = content


class WholeFormatter:
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormatter(WholeFormatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]


class Printer:
    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


base_formatter = WholeFormatter()
new_formatter = ReverseFormatter()

book = Book("Yay, new book!")
printer = Printer()

print(printer.get_book(book, base_formatter))
print(printer.get_book(book, new_formatter))
