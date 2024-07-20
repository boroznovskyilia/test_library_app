from models.repository import LibraryRepository
from models.models import Book
from utils.errors import BookAlreadyExistsException,NoBookExeption
from dataclasses import dataclass

@dataclass
class LibraryService():
    repository:LibraryRepository
    
    def add(self,book:Book):
        try:
            self.repository.add(book)
            return "Book added successfully"
        except BookAlreadyExistsException:
            return f"Book with this title - {book.title},author - {book.author} and year - {book.year} already exists"
    def get_all(self):
        return self.repository.get_all()
    def search_by_field(self,search_field:str,search_value:str):
        try:
            searched_book = self.repository.search_by_field(search_field,search_value)
            return searched_book
        except NoBookExeption:
            return (f"No book found with {search_field} - {search_value}")
    
    def change_status(self, book_id:str):
        try:
            changed_book = self.repository.change_status(book_id)
            return f"Book with id {changed_book.id} status changed to {changed_book.status}"
        except NoBookExeption:
            return f"No book found with id - {book_id}"
    
    def delete(self, book_id:str):
        try:
            self.repository.delete(book_id)
            return f"Book with id - {book_id} deleted successfully"
        except NoBookExeption:
            return f"No book found with id - {book_id}"