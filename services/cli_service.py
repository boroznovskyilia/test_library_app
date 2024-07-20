from services.library_service import LibraryService
from models.models import Book,Library
from dataclasses import dataclass
import json

@dataclass
class CliCervice():
    library_servise:LibraryService
    
    def start(self):
        while True:
            choice = self.show_menu()
            

            if choice == "0":
                break
            elif choice == "1":
                self.add_book()
            elif choice == "2":
                self.get_all_books()
            elif choice == "3":
                self.search_book_by_field()
            elif choice == "4":
                self.change_book_status()
            elif choice == "5":
                self.delete_book()
            else:
                print("Invalid choice. Please try again.")
    
    def show_menu(self):
        print("\n\n")
        print("Library management system")
        print("1. Add book")
        print("2. Get all books")
        print("3. Search book by field")
        print("4. Change book status")
        print("5. Delete book")
        print("0. Exit")
        choice = input("Enter your choice: ")
        print("\n\n")
        return choice

    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")
        try:
            year = int(year)
            if author.strip() == "" or book_title.strip() == "" or year < 0:
                print("Invalid input. Title, author, and year must be provided. And year must be > = 0")
                return
            book = Book(book_title, author, year)
        except ValueError:
            print("Invalid year format. Please enter a valid year.")
            return
        print(self.library_servise.add(book))

    def get_all_books(self):
        books = self.library_servise.get_all()
        if not books:
            print("No books found.")
            return

        for i,book in enumerate(books):
            if i == 0:
                print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*book.__dict__.keys()))
            print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*book.__dict__.values()))
    
    def search_book_by_field(self):
        search_field = input("Enter field to search (title, author, year): ")
        search_value = input("Enter value to search: ")
        if search_field not in["title","author","year"]:
            print ("Search field should be one of the following:title,author,year")
            return
        result = self.library_servise.search_by_field(search_field, search_value)
        if isinstance(result, Book):
            print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*result.__dict__.keys()))
            print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*result.__dict__.values()))
        else:
            print(result)
    
    def change_book_status(self):
        book_id = input("Enter book id: ")
        print(self.library_servise.change_status(book_id))
    
    def delete_book(self):
        book_id = input("Enter book id: ")
        print(self.library_servise.delete(book_id))