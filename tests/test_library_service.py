from models.models import Library, Book
import pytest
from models.repository import LibraryRepository
from services.library_service import LibraryService
from unittest import mock
from utils.errors import BookAlreadyExistsException,NoBookExeption


@pytest.fixture
def library():
    return Library()

@pytest.fixture
def book():
    return Book("Sample Book", "Sample Author", 2021)

@pytest.fixture
def repository(library):
    return LibraryRepository(library)

@pytest.fixture
def service(repository):
    return LibraryService(repository)
    

@mock.patch.object(LibraryRepository, 'add')
def test_add_book_success(mock_add:mock.Mock, service:LibraryService, book:Book):
    mock_add.return_value = None 
    result = service.add(book)
    assert result == "Book added successfully"
    mock_add.assert_called_once_with(book)

@mock.patch.object(LibraryRepository, 'add')
def test_add_book_already_exists(mock_add:mock.Mock, service:LibraryService, book:Book):
    mock_add.side_effect = BookAlreadyExistsException()  
    result = service.add(book)
    assert result == f"Book with this title - {book.title},author - {book.author} and year - {book.year} already exists"
    mock_add.assert_called_once_with(book)


@mock.patch.object(LibraryRepository, 'get_all')
def test_get_all_books(mock_get_all:mock.Mock, service:LibraryService):
    mock_get_all.return_value = [
        Book("Sample Book 1", "Sample Author", 2021),
        Book("Sample Book 2", "Another Author", 2020)
    ]
    books = service.get_all()
    assert len(books) == 2
    assert books[0].title == "Sample Book 1"
    assert books[1].title == "Sample Book 2"
    mock_get_all.assert_called_once()

@mock.patch.object(LibraryRepository, 'search_by_field')
def test_search_by_field_success(mock_search_by_field:mock.Mock, service:LibraryService, book:Book):
    mock_search_by_field.return_value = book  # Simulating successful search
    result = service.search_by_field("title", "Sample Book")
    assert result == book
    mock_search_by_field.assert_called_once_with("title", "Sample Book")

@mock.patch.object(LibraryRepository, 'search_by_field')
def test_search_by_field_not_found(mock_search_by_field:mock.Mock, service:LibraryService,):
    mock_search_by_field.side_effect = NoBookExeption()  # Simulating book not found scenario
    result = service.search_by_field("title", "Nonexistent Book")
    assert result == "No book found with title - Nonexistent Book"
    mock_search_by_field.assert_called_once_with("title", "Nonexistent Book")

@mock.patch.object(LibraryRepository, 'change_status')
def test_change_status_success(mock_change_status:mock.Mock, service:LibraryService, book:Book):
    book.status = "выдана"
    mock_change_status.return_value = book 
    result = service.change_status(book.id)
    assert result == f"Book with id {book.id} status changed to выдана"
    assert book.status == "выдана"
    mock_change_status.assert_called_once_with(book.id)

@mock.patch.object(LibraryRepository, 'change_status')
def test_change_status_not_found(mock_change_status:mock.Mock, service:LibraryService,):
    mock_change_status.side_effect = NoBookExeption() 
    result = service.change_status("nonexistent_id")
    assert result == "No book found with id - nonexistent_id"
    mock_change_status.assert_called_once_with("nonexistent_id")

@mock.patch.object(LibraryRepository, 'delete')
def test_delete_success(mock_delete:mock.Mock, service:LibraryService, book:Book):
    mock_delete.return_value = None 
    result = service.delete(book.id)
    assert result == f"Book with id - {book.id} deleted successfully"
    mock_delete.assert_called_once_with(book.id)

@mock.patch.object(LibraryRepository, 'delete')
def test_delete_not_found(mock_delete:mock.Mock, service:LibraryService,):
    mock_delete.side_effect = NoBookExeption()
    result = service.delete("nonexistent_id")
    assert result == "No book found with id - nonexistent_id"
    mock_delete.assert_called_once_with("nonexistent_id")