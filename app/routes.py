from flask import render_template, request, redirect, url_for
from app import app
from app.db import db
from app.dao import BookDao, AuthorDao, GenreDao, MediumDao
import logging

from app.models import Book, Author, DisplayBooksResponseItem, Genre


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        cursor = db.cursor()

        try:
            title = request.form['title']
            read_status = int(request.form.get('read_status', 0))  # Convert to integer (1 for "Read", 0 for "Unread")
            isbn = request.form.get('isbn', None)
            description = request.form.get('description', None)
            image_url = request.form.get('image_url', None)
            external_url = request.form.get('external_url', None)

            # AUTHOR
            # Check if the user selected an existing author or is adding a new one
            if 'existing_author' in request.form:
                author_id = request.form['existing_author']
            else:
                # If adding a new author, insert into authors table
                author_first_name = request.form['author_first_name']
                author_last_name = request.form['author_last_name']

                # Print debug
                logging.debug(
                    f"In routes add_books - Trying to get author_id for: {author_first_name} {author_last_name}")

                author = Author(author_first_name, author_last_name)
                author_id = AuthorDao.get_id(author)
                logging.debug(f"In routes add_books - Retrieved author_id: {author_id}")

                if not author_id:
                    author_id = AuthorDao.insert_item(author)
                    logging.debug(f"In routes add_books - Inserted author_id: {author_id}")

            # GENRE
            # Check if the user selected an existing genre or is adding a new one
            if 'existing_genre' in request.form:
                genre_id = request.form['existing_genre']
            else:
                # If adding a new genre, insert into genres table
                new_genre = request.form.get('new_genre', None)
                genre_id = GenreDao.get_id(new_genre)
                if not genre_id and new_genre is not None:
                    genre_id = GenreDao.insert_item(Genre(new_genre))
                    logging.debug(f"In routes add_books - genre_id: {genre_id}")

            # Medium
            # Get medium_id based on medium_name
            medium_name = request.form['medium']
            medium_id = MediumDao.get_id(medium_name)
            logging.debug(f"In routes add_books - Selected medium ID: {medium_id}")

            # Insert book into the database
            new_book = Book(title, author_id, read_status, isbn, description, image_url, external_url, medium_id,
                            genre_id)
            book_id = BookDao.insert_item(new_book)
            logging.info(f"In routes add_books - Book added successfully! {book_id}")
        except Exception as e:
            # An error occurred, rollback the transaction and handle the error
            db.rollback()
            logging.error(f"In routes add_books - Error: {str(e)}")
        finally:
            cursor.close()
        return redirect(url_for('home'))

    return render_template('add_book.html')


@app.route('/display_books')
def display_books():
    cursor = db.cursor()

    try:
        # Retrieve books from the database with author information
        books = BookDao.get_all_items()

        for book in books:
            logging.debug(
                f"In routes display_books - Processed book for display: {book.__str__()}")

        return render_template('display_books.html', books=books)
    except Exception as e:
        logging.error(f"In routes display_books - Error retrieving and displaying books: {str(e)}")
    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(debug=False)
