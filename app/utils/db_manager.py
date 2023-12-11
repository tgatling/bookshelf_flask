from app.db import cursor, db
from app.models.book import Book
from app.utils.error_handler import ErrorHandler


class DatabaseManager:
    @staticmethod
    def add_book(self, book):
        try:
            query = """
                INSERT INTO books 
                (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (book.title, book.author_id, book.read_status, book.isbn, book.description,
                      book.image_url, book.external_url, book.media_id, book.genre_id)

            cursor.execute(query, values)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            ErrorHandler.handle_error(e)
            return False
        finally:
            cursor.close()

    @staticmethod
    def get_books(self):
        try:
            cursor.execute("""
                SELECT books.title, authors.first_name, authors.last_name, books.read_status, media.media_name
                FROM books 
                JOIN authors ON books.author_id = authors.author_id
                JOIN media ON books.media_id = media.media_id
                JOIN genres ON books.genre_id = genres.genre_id
            """)
            books_data = cursor.fetchall()

            books = [
                Book(title, author_first_name, author_last_name, read_status, media)
                for title, author_first_name, author_last_name, read_status, media in books_data
            ]

            return books
        except Exception as e:
            ErrorHandler.handle_error(e)
            return []
