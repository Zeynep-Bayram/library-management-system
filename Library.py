"""
Author:Zeynep Bayram
Project:Library Management System
"""

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):   # type: ignore
        self.file.close()

    def books_list(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("The book was not found in the system.")
            return
        print("List of Books:")
        for book in books:
            book_info = book.strip().split(",")
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter first year of publication: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title not in book:
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print("The book is not available in the system.")
            return
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book removed successfully!")

lib = Library()

# Menu
while True:
    print("**** MENU ****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.books_list()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
