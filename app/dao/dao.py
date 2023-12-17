from app.db import cursor, db
from app.models import DisplayBooksResponseItem, Book, Author, Genre, Medium
import logging


class BaseDao:

    @staticmethod
    def get_id(item):
        pass

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(item):
        pass


class ModificationDao:

    @staticmethod
    def update_item(item):
        pass

    @staticmethod
    def delete_item(item):
        pass


class BookDao(BaseDao, ModificationDao):

    @staticmethod
    def get_id(book):
        logging.debug(f"In BookDao.get_id - book.title: {book.title}, book.medium_id: {book.medium_id}")
        query = "SELECT book_id FROM  books WHERE title = %s AND medium_id = %s"
        cursor.execute(query, (book.title, book.medium_id))
        result = cursor.fetchone()
        book_id = result[0] if result else None
        logging.debug(f"In BookDao.get_id - Returned book_id: {book_id}")
        return book_id

    @staticmethod
    def get_all_items():
        cursor.execute("""
                SELECT books.book_id, books.title, authors.first_name, authors.last_name, books.read_status,
                       medium.medium_name, books.isbn, books.description, books.image_url, books.external_url,
                       genres.genre_name
                FROM books 
                LEFT JOIN authors ON books.author_id = authors.author_id
                LEFT JOIN medium ON books.medium_id = medium.medium_id
                LEFT JOIN genres ON books.genre_id = genres.genre_id
            """)
        books_data = cursor.fetchall()

        logging.debug(f"In BookDao.get_all_items - books_data: {books_data}")

        books = [
            DisplayBooksResponseItem(book_id, title, author_first_name, author_last_name, read_status, medium, isbn,
                                     description, image_url,
                                     external_url, genre)
            for book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
            external_url, genre
            in books_data
        ]

        for book in books:
            logging.debug(
                f"In BookDao.get_all_items - Retrieved book: {book.__str__()}")

        return books

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(book: Book):
        logging.debug(f"In BookDao.insert_item - New book: {book.__str__()}")
        query = """
                INSERT INTO books 
                (title, author_id, read_status, isbn, description, image_url, external_url, medium_id, genre_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
        cursor.execute(query, (
            book.title, book.author_id, book.read_status, book.isbn, book.description, book.image_url,
            book.external_url, book.medium_id, book.genre_id,))
        db.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        book_id = cursor.fetchone()[0]

        logging.info(f"In BookDao.insert_item - Book added successfully! book_id: {book_id}")

        return book_id


class AuthorDao(BaseDao):

    @staticmethod
    def get_id(author):
        logging.debug(
            f"In AuthorDao.get_id - author.first_name: {author.first_name}, author.last_name: {author.last_name}")

        query = "SELECT author_id FROM authors WHERE first_name = %s AND last_name = %s"
        cursor.execute(query, (author.first_name, author.last_name,))
        result = cursor.fetchone()
        author_id = result[0] if result else None

        logging.debug(f"In AuthorDao.get_id - Returned author_id: {author_id}")

        return author_id

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(author: Author):
        logging.debug(
            f"In AuthorDao.insert_item - author first_name: {author.first_name}, last_name: {author.last_name}")

        query = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s)"
        cursor.execute(query, (author.first_name, author.last_name,))
        db.commit()

        # Retrieve the newly inserted author's ID
        cursor.execute("SELECT LAST_INSERT_ID()")
        author_id = cursor.fetchone()[0]

        logging.info(f"In AuthorDao.insert_item - Author added successfully! {author_id}")

        return author_id


class GenreDao(BaseDao):

    @staticmethod
    def get_id(genre_name):
        logging.debug(f"In GenreDao.get_id - genre_name: {genre_name}")

        query = "SELECT genre_id FROM genres WHERE genre_name = %s"
        cursor.execute(query, (genre_name,))
        result = cursor.fetchone()
        genre_id = result[0] if result else None

        logging.debug(f"In GenreDao.get_id - Returned genre_id: {genre_id}")

        return genre_id

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(genre: Genre):
        query = "INSERT INTO genres (genre_name) VALUES (%s)"
        cursor.execute(query, (genre.genre_name,))
        db.commit()

        # Retrieve the newly inserted genre's ID
        cursor.execute("SELECT LAST_INSERT_ID()")
        genre_id = cursor.fetchone()[0]

        logging.debug(f"In GenreDao.insert_id - Returned genre_id: {genre_id}")

        return genre_id


class MediumDao(BaseDao):

    @staticmethod
    def get_id(medium_name):
        logging.debug(f"In MediumDao.get_id - genre_name: {medium_name}")

        query = "SELECT medium_id FROM medium WHERE medium_name = %s"
        cursor.execute(query, (medium_name,))
        result = cursor.fetchone()
        medium_id = result[0] if result else None

        logging.debug(f"In MediumDao.get_id - Returned medium_id: {medium_id}")

        return medium_id

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(medium: Medium):
        query = "INSERT INTO medium (medium_name) VALUES (%s)"
        cursor.execute(query, (medium.medium_name,))
        db.commit()

        # Retrieve the newly inserted genre's ID
        cursor.execute("SELECT LAST_INSERT_ID()")
        medium_id = cursor.fetchone()[0]

        logging.debug(f"In MediumDao.insert_id - Returned medium_id: {medium_id}")

        return medium_id
