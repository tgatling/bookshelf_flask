from unittest import mock
from app.dao.dao import BookDao, AuthorDao, GenreDao, MediumDao
from app.models import Book, Author, Genre, Medium, DisplayBooksResponseItem
import pytest

mock_book_id = 1
mock_title = "Test Title"
mock_reading_status = 1
mock_isbn = 1234567890
mock_description = "This is a test book description"
mock_image_url = "https://example.com/image.jpg"
mock_external_url = "https://example.com/"
mock_author_id = 1
mock_genre_id = 1
mock_medium_id = 1

mock_author_first_name = "Test"
mock_author_last_name = "Author"
mock_genre = "Programming"
mock_medium = "Ebook"

mock_book = Book(mock_title, mock_reading_status, mock_isbn, mock_description, mock_image_url, mock_external_url,
                 mock_author_id, mock_genre_id, mock_medium_id)

mock_display_book_response_item = DisplayBooksResponseItem(mock_book_id, mock_title, mock_author_first_name,
                                                           mock_author_last_name, mock_reading_status, mock_medium,
                                                           mock_isbn, mock_description, mock_image_url,
                                                           mock_external_url, mock_genre)


# Define a fixture that will be used to mock db
@pytest.fixture
def mock_db():
    mock_cursor = mock.MagicMock()
    mock_db = mock.MagicMock()

    mock_db.cursor.return_value = mock_cursor
    mock_db.fetchone.return_value = {
        'book_id': 1,
        'title': 'Test Book',
        'author_id': 1,
        # add all other book fields here
    }
    return mock_db


def test_book_dao_get_id(mock_db):
    with mock.patch('app.dao.dao.db', new=mock_db):
        book_id = BookDao.get_id(mock_book)

        mock_db.cursor.assert_called_once()
        mock_db.execute.assert_called_once_with("SELECT book_id FROM  books WHERE title = %s AND medium_id = %s",
                                                (mock_book.title, mock_book.medium_id))
        mock_db.fetchone.assert_called_once()

        assert book_id == mock_book.book_id

# def test_book_dao_get_item(mock_db):
#     # Assume that db is your actual database object that needs to be mocked
#     with mock.patch('app.dao.dao.db', new=mock_db):
#         book_id = 1
#         book = BookDao.get_item(book_id)
#
#         mock_db.cursor.assert_called_once()
#         mock_db.execute.assert_called_once_with("SELECT * FROM books WHERE books.book_id = %s", (book_id,))
#         mock_db.fetchone.assert_called_once()
#
#         # Now check if returned book is as per expectation
#         assert book['id'] == 1
#         assert book['title'] == 'Test Book'
#         assert book['author_id'] == 1
