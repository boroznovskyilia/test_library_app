import json
from models.models import Book,Library


class BoookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return obj.__dict__
        return super().default(obj)


class LibraryEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Library):
            books = []
            for book in obj.books:
                books.append(book.__dict__)
            return books
        return super().default(obj)