from app.db import cursor
from app.models import Book


# def get_all_books():
#     cursor.execute("""
#             SELECT books.book_id, books.title, authors.first_name, authors.last_name, books.read_status,
#                    medium.medium_name, books.isbn, books.description, books.image_url, books.external_url,
#                    genres.genre_name
#             FROM books
#             JOIN authors ON books.author_id = authors.author_id
#             JOIN medium ON books.medium_id = medium.medium_id
#             JOIN genres ON books.genre_id = genres.genre_id
#         """)
#     books_data = cursor.fetchall()
#
#     books = [
#         Book(book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
#              external_url, genre)
#         for book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description, image_url,
#         external_url, genre
#         in books_data
#     ]
#
#     return books


def get_author_id(author_first_name, author_last_name):
    query = "SELECT author_id FROM authors WHERE first_name = %s AND last_name = %s"
    cursor.execute(query, (author_first_name, author_last_name))
    result = cursor.fetchone()
    author_id = result[0] if result else None
    return author_id


def get_genre_id(genre_name):
    query = "SELECT genre_id FROM genres WHERE genre_name = %s"
    cursor.execute(query, (genre_name,))
    result = cursor.fetchone()
    genre_id = result[0] if result else None
    return genre_id


def get_medium_id(medium_name):
    query = "SELECT medium_id FROM medium WHERE medium_name = %s"
    cursor.execute(query, (medium_name,))
    result = cursor.fetchone()
    medium_id = result[0] if result else None
    return medium_id
