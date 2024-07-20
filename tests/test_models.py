import pytest
from models.models import Book, Library


def test_book_creation():
    book = Book("asdf","asdf",123)
    assert book.title == "asdf"
    assert book.author == "asdf"
    assert book.year == 123


def test_library_creation():
    library = Library()
    assert library.books == None