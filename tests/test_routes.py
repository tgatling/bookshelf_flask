import pytest
from unittest.mock import patch, MagicMock
from app.routes import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    """Test if the index route is accessible"""
    res = client.get('/')
    assert res.status_code == 200


def test_add_book_get_request(client):
    """Test if the add_book route is accessible via GET and renders the correct template"""
    res = client.get('/add_book')
    assert res.status_code == 200
    assert b"Add Book" in res.data


@patch('app.routes.AuthorDao.get_id')
@patch('app.routes.AuthorDao.insert_item')
@patch('app.routes.GenreDao.get_id')
@patch('app.routes.GenreDao.insert_item')
@patch('app.routes.MediumDao.get_id')
@patch('app.routes.BookDao.insert_item')
def test_add_book_with_new_author_genre_post_request(mock_book_insert, mock_medium_get_id, mock_genre_insert,
                                                     mock_genre_get_id, mock_author_insert, mock_author_get_id, client):
    """Test if a book with new author and new genre is added"""

    # Configure the mocks
    mock_author_get_id.return_value = None
    mock_author_insert.return_value = 1
    mock_genre_get_id.return_value = None
    mock_genre_insert.return_value = 1
    mock_medium_get_id.return_value = 1
    mock_book_insert.return_value = 1

    mock_data = {
        "title": "Test Book",
        "read_status": 1,
        "isbn": "1234567890",
        "description": "This is a test book description",
        "image_url": "https://example.com/image.jpg",
        "external_url": "https://example.com/",
        "author_first_name": "Test",
        "author_last_name": "Author",
        "new_genre": "1",
        "medium": "1"
    }

    res = client.post('/add_book', data=mock_data)
    # checks that your add_book redirects correctly
    assert res.status_code == 302
    assert res.location.endswith("/")
    # checks that your mocked db operations have been called
    mock_author_get_id.assert_called_once()
    mock_author_insert.assert_called_once()
    mock_genre_get_id.assert_called_once()
    mock_genre_insert.assert_called_once()
    mock_medium_get_id.assert_called_once()
    mock_book_insert.assert_called_once()


@patch('app.routes.AuthorDao.get_id')
@patch('app.routes.AuthorDao.insert_item')
@patch('app.routes.GenreDao.get_id')
@patch('app.routes.GenreDao.insert_item')
@patch('app.routes.MediumDao.get_id')
@patch('app.routes.BookDao.insert_item')
def test_add_book_with_existing_author_genre_post_request(mock_book_insert, mock_medium_get_id, mock_genre_insert,
                                                          mock_genre_get_id, mock_author_insert, mock_author_get_id,
                                                          client):
    """Test if a book with existing author and genre is added"""

    # Configure the mocks
    mock_author_get_id.return_value = 1
    mock_author_insert.return_value = 1
    mock_genre_get_id.return_value = 1
    mock_genre_insert.return_value = 1
    mock_medium_get_id.return_value = 1
    mock_book_insert.return_value = 1

    mock_data = {
        "title": "Test Book",
        "read_status": 1,
        "isbn": "1234567890",
        "description": "This is a test book description",
        "image_url": "https://example.com/image.jpg",
        "external_url": "https://example.com/",
        "existing_author": "Test Author",
        "existing_genre": "Ebook",
        "medium": "1"
    }

    res = client.post('/add_book', data=mock_data)
    # checks that your add_book redirects correctly
    assert res.status_code == 302
    assert res.location.endswith("/")
    # checks that your mocked db operations have been called
    mock_author_get_id.assert_not_called()
    mock_author_insert.assert_not_called()
    mock_genre_get_id.assert_not_called()
    mock_genre_insert.assert_not_called()
    mock_medium_get_id.assert_called_once()
    mock_book_insert.assert_called_once()


@patch('app.routes.BookDao.get_all_items')
def test_display_books_ebook(mock_get_all_items, client):
    """Test the display_books route"""

    # Create a mock book object
    mock_ebook = {
        "title": "Test Ebook",
        "read_status": 1,
        "isbn": "1234567890",
        "description": "This is a test book description",
        "image_url": "https://example.com/image.jpg",
        "external_url": "https://example.com/",
        "author_first_name": "Test",
        "author_last_name": "Author",
        "genre": "1",
        "medium": "Ebook"
    }

    # Configure the mock to return a list of one book when called.
    mock_get_all_items.return_value = [mock_ebook]

    res = client.get('/display_books')

    assert res.status_code == 200
    assert b"Test Ebook" in res.data


@patch('app.routes.BookDao.get_all_items')
def test_display_books_audiobook(mock_get_all_items, client):
    """Test the display_books route"""

    # Create a mock book object
    mock_audiobook = {
        "title": "Test Audiobook",
        "read_status": 1,
        "isbn": "1234567890",
        "description": "This is a test book description",
        "image_url": "https://example.com/image.jpg",
        "external_url": "https://example.com/",
        "author_first_name": "Test",
        "author_last_name": "Author",
        "genre": "1",
        "medium": "Ebook"
    }

    # Configure the mock to return a list of one book when called.
    mock_get_all_items.return_value = [mock_audiobook]

    res = client.get('/display_books')

    assert res.status_code == 200
    assert b"Test Audiobook" in res.data


@patch('app.routes.BookDao.get_all_items')
def test_display_books_physical(mock_get_all_items, client):
    """Test the display_books route"""

    # Create a mock book object
    mock_ebook = {
        "title": "Test Physical Book",
        "read_status": 1,
        "isbn": "1234567890",
        "description": "This is a test book description",
        "image_url": "https://example.com/image.jpg",
        "external_url": "https://example.com/",
        "author_first_name": "Test",
        "author_last_name": "Author",
        "genre": "1",
        "medium": "Physical"
    }

    # Configure the mock to return a list of one book when called.
    mock_get_all_items.return_value = [mock_ebook]

    res = client.get('/display_books')

    assert res.status_code == 200
    assert b"Test Physical Book" in res.data
