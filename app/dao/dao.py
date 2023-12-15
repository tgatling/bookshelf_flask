from app.db import cursor
from app.models import DisplayBooksResponseItem, Book, Author, Genre, Medium


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
        query = "SELECT book_id FROM  books WHERE title = %s AND medium_id = %s"
        cursor.execute(query, (book.title, book.medium_id))
        result = cursor.fetchone()
        book_id = result[0] if result else None
        return book_id

    @staticmethod
    def get_all_items():
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
            DisplayBooksResponseItem(book_id, title, author_first_name, author_last_name, read_status, medium, isbn,
                                     description, image_url,
                                     external_url, genre)
            for book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
            external_url, genre
            in books_data
        ]

        return books

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(book: Book):
        query = """
                INSERT INTO books 
                (title, author_id, read_status, isbn, description, image_url, external_url, medium_id, genre_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
        cursor.execute(query, book)
        cursor.connection.commit()


class AuthorDao(BaseDao):

    @staticmethod
    def get_id(author):
        query = "SELECT author_id FROM authors WHERE first_name = %s AND last_name = %s"
        cursor.execute(query, (author.first_name, author.last_name))
        result = cursor.fetchone()
        author_id = result[0] if result else None
        return author_id

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(author: Author):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s)"
        cursor.execute(query, (author,))
        cursor.connection.commit()

        # Retrieve the newly inserted author's ID
        cursor.execute("SELECT LAST_INSERT_ID()")
        author_id = cursor.fetchone()[0]
        return author_id


class GenreDao(BaseDao):

    @staticmethod
    def get_id(genre_name):
        query = "SELECT genre_id FROM genres WHERE genre_name = %s"
        cursor.execute(query, (genre_name,))
        result = cursor.fetchone()
        genre_id = result[0] if result else None
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
        cursor.execute(query, (genre,))
        cursor.connection.commit()

        # Retrieve the newly inserted genre's ID
        cursor.execute("SELECT LAST_INSERT_ID()")
        genre_id = cursor.fetchone()[0]
        return genre_id


class MediumDao(BaseDao):

    @staticmethod
    def get_id(medium_name):
        query = "SELECT medium_id FROM medium WHERE medium_name = %s"
        cursor.execute(query, (medium_name,))
        result = cursor.fetchone()
        medium_id = result[0] if result else None
        return medium_id

    @staticmethod
    def get_all_items():
        pass

    @staticmethod
    def get_item(item_id: int):
        pass

    @staticmethod
    def insert_item(medium: Medium):
        pass
