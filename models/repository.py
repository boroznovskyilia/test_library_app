from copy import deepcopy
import json
from dataclasses import dataclass
from models.models import Library, Book
from utils.consts import STORAGE_PATH
from utils.encoders import BoookEncoder,LibraryEncoder
from utils.errors import BookAlreadyExistsException,NoBookExeption


@dataclass
class LibraryRepository:      
    library:Library
       
    def get_all(self) -> list[Book]:
        books = []
        try:
            with open(STORAGE_PATH, "r") as file:
                books = [Book(**book) for book in json.load(file)]
        except FileNotFoundError:
            with open(STORAGE_PATH, "w+") as file:
                json.dump([],file)
        return books
    
    def get(self,book_id:str) -> Book|None:
        books = self.get_all()
        for book in books:
            if book.id == book_id:
                return book
        return None

    def book_already_exist(self,checking_book:Book) -> bool:
        books:list[Book] = self.get_all()
        exists:bool = False
        
        for book in books:
            if (book.title == checking_book.title 
                and book.author == checking_book.author 
                and book.year == checking_book.year
                ):
                exists = True
                break

        return exists

    def add(self,book:Book) -> None:
        if self.book_already_exist(book):
            raise BookAlreadyExistsException()
        self.library.books = self.get_all()
        self.library.books.append(book)
        with open(STORAGE_PATH,"w") as file:
            json.dump(self.library,file,cls=LibraryEncoder,ensure_ascii=False,indent=4,separators=(',',': '))
    
    def search_by_field(self,search_field:str,search_value:str) -> Book:
        books = self.get_all()
        for book in books:
            if book.__dict__[search_field] == search_value:
                return book
        raise NoBookExeption()

    def delete(self, book_id:str) -> None:
        book = self.get(book_id)
        if book is None:
            raise NoBookExeption()
        self.library.books = self.get_all()
        self.library.books.remove(book)
        with open(STORAGE_PATH,"w") as file:
            json.dump(self.library,file,cls=LibraryEncoder,ensure_ascii=False,indent=4,separators=(',',': '))
    
    def change_status(self,book_id:str) -> Book:
        book = self.get(book_id)
        if book is None:
            raise NoBookExeption()
        new_book = deepcopy(book)
        if new_book.status == "в наличии":
            new_book.status = "выдана"
        else:
            new_book.status = "в наличии"
        self.library.books = self.get_all()
        self.library.books.remove(book)
        self.library.books.append(new_book)
        with open(STORAGE_PATH,"w") as file:
            json.dump(self.library,file,cls=LibraryEncoder,ensure_ascii=False,indent=4,separators=(',',': '))
        return new_book