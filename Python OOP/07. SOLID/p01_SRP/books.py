from typing import Optional, List


class Book:
    def __init__(self, title: str, author: str, total_pages: int) -> None:
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def turn_page(self, new_page: int) -> None:
        self.current_page = new_page

    def __repr__(self):
        return f"\"{self.title}\" by {self.author} ({self.total_pages} pages)"


class Library:
    def __init__(self, name: str, books: list[Book]) -> None:
        self.name = name
        self.books = books

    def add_book(self, book: Book) -> Optional[str]:
        if book in self.books:
            raise ValueError("Book already in library!")
        self.books.append(book)
        return f"Successfully added book {book}"

    def remove_book(self, book_title: str, book_author: str) -> Optional[str]:
        wanted_book = [x for x in self.books if x.title == book_title and x.author == book_author]
        if not wanted_book:
            raise ValueError(f"There is no \"{book_title}\" by {book_author} in this library.")
        self.books.remove(wanted_book[0])
        return f"Successfully removed book {wanted_book[0]}"

    def get_author_books(self, author_name: str) -> List[Book]:
        return [x for x in self.books if x.author == author_name]

    def __len__(self):
        return len(self.books)


if __name__ == "__main__":
    book_one = Book("A", "Alphabet", 1)
    book_two = Book("Z", "Alphabet", 1)
    library = Library("PyLibrary", [book_one, book_two])

    print(len(library))
    print(library.get_author_books("Alphabet"))
    print(library.get_author_books("A"))

    book_three = Book("0", "Numbers", 1)
    print(library.add_book(book_three))
    print(library.remove_book("A", "Alphabet"))
