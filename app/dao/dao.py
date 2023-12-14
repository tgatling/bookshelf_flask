from app.db import cursor
from app.models import Book


class BaseDao:
    pass


class BookDao(BaseDao):
    @staticmethod
    def get_all_books():
        cursor.execute("""
                SELECT books.book_id, books.title, authors.first_name, authors.last_name, books.read_status,
                       medium.medium_name, books.isbn, books.description, books.image_url, books.external_url,
                       genres.genre_name
                FROM books 
                JOIN authors ON books.author_id = authors.author_id
                JOIN medium ON books.medium_id = medium.medium_id
                JOIN genres ON books.genre_id = genres.genre_id
            """)
        books_data = cursor.fetchall()

        books = [
            Book(book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
                 external_url, genre)
            for book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
            external_url, genre
            in books_data
        ]

        return books


class AuthorDao(BaseDao):
    pass
