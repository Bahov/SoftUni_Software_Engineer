ani_book = input()
book_input = input()

books_checked = 0
while book_input != "No More Books" and book_input != ani_book:
    books_checked += 1
    book_input = input()

if book_input == ani_book:
    print(f"You checked {books_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
