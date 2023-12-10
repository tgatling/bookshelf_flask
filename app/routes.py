from flask import render_template, request, redirect, url_for, flash
from app import app
from app.db import cursor, db
from app.database_functions import get_author_id, get_genre_id, get_media_id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_book', methods=['POST'])
def add_book():
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

            # Print debug information
            print(f"Trying to get author_id for: {author_first_name} {author_last_name}")

            author_id = get_author_id(author_first_name, author_last_name)
            print(f"Retrieved author_id: {author_id}")

            if not author_id:
                cursor.execute(
                    "INSERT INTO authors (first_name, last_name) VALUES (%s, %s)",
                    (author_first_name, author_last_name)
                )
                db.commit()

                # Retrieve the newly inserted author's ID
                cursor.execute("SELECT LAST_INSERT_ID()")
                author_id = cursor.fetchone()[0]
                print(f"Inserted author_id: {author_id}")

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
                genre_id = cursor.fetchone()[0]  # Fetch the correct ID here
                print(f"genre_id: {genre_id}")

        # MEDIA
        # Get media_id based on media_name
        media = request.form['media']
        media_id = get_media_id(media)
        print(f"Selected Media ID: {media_id}")

        # Insert book into the database
        query = """
            INSERT INTO books 
            (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id)
        print(f"values: {values}")
        cursor.execute(query, values)
        db.commit()
        flash("Book added successfully!", "success")
    except Exception as e:
        # An error occurred, rollback the transaction and handle the error
        db.rollback()
        flash(f"Error: {str(e)}", "danger")
        print(f"Error: {str(e)}", "danger")
    finally:
        cursor.close()

    return redirect(url_for('index'))


@app.route('/display_books')
def display_books():
    # Retrieve books from the database with author information
    cursor.execute("""
        SELECT books.title, authors.first_name, authors.last_name, books.read_status, media.media_name
        FROM books 
        JOIN authors ON books.author_id = authors.author_id
        JOIN media ON books.media_id = media.media_id
    """)
    books_data = cursor.fetchall()

    books = [
        {"title": title, "author_first_name": author_first_name, "author_last_name": author_last_name,
         "read_status": read_status, "media": media}
        for title, author_first_name, author_last_name, read_status, media in books_data
    ]

    return render_template('display_books.html', books=books)


if __name__ == "__main__":
    app.run(debug=True)
