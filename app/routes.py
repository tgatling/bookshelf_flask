from flask import render_template, request, redirect, url_for
from app import app
from app.db import db
from app.database_functions import get_author_id, get_genre_id, get_media_id, get_all_books
import logging


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
                    f"In function add_books: Trying to get author_id for: {author_first_name} {author_last_name}")

                author_id = get_author_id(author_first_name, author_last_name)
                logging.debug(f"In function add_books: Retrieved author_id: {author_id}")

                if not author_id:
                    cursor.execute(
                        "INSERT INTO authors (first_name, last_name) VALUES (%s, %s)",
                        (author_first_name, author_last_name)
                    )
                    db.commit()

                    # Retrieve the newly inserted author's ID
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    author_id = cursor.fetchone()[0]
                    logging.debug(f"In function add_books: Inserted author_id: {author_id}")

            # GENRE
            # Check if the user selected an existing genre or is adding a new one
            if 'existing_genre' in request.form:
                genre_id = request.form['existing_genre']
            else:
                # If adding a new genre, insert into genres table
                new_genre = request.form.get('new_genre', None)
                genre_id = get_genre_id(new_genre)
                if not genre_id:
                    cursor.execute(
                        "INSERT INTO genres (genre_name) VALUES (%s)",
                        (new_genre,)
                    )
                    db.commit()

                    # Retrieve the newly inserted genre's ID
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    genre_id = cursor.fetchone()[0]
                    logging.debug(f"In function add_books: genre_id: {genre_id}")

            # MEDIA
            # Get media_id based on media_name
            media = request.form['media']
            media_id = get_media_id(media)
            logging.debug(f"In function add_books: Selected Media ID: {media_id}")

            # Insert book into the database
            query = """
                INSERT INTO books 
                (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id)
            logging.debug(f"In function add_books: values: {values}")

            cursor.execute(query, values)
            db.commit()
            logging.info(f"In function add_books: Book added successfully! {values}")
        except Exception as e:
            # An error occurred, rollback the transaction and handle the error
            db.rollback()
            logging.error(f"In function add_books: Error: {str(e)}")
        finally:
            cursor.close()
        return redirect(url_for('home'))

    return render_template('add_book.html')


@app.route('/display_books')
def display_books():
    cursor = db.cursor()

    try:
        # Retrieve books from the database with author information
        books = get_all_books()

        logging.debug(f"In display_books function: Processed books for display: {books}")

        return render_template('display_books.html', books=books)
    except Exception as e:
        logging.error(f"In display_books function: Error retrieving and displaying books: {str(e)}")
    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(debug=True)
