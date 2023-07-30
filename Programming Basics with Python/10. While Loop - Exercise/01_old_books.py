wanted_book = input()
found_book = input()

books_checked = 0

while found_book != wanted_book:
    books_checked += 1
    found_book = input()
    if found_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break
else:
    print(f"You checked {books_checked} books and found it.")
