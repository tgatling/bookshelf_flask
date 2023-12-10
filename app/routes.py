from flask import render_template, request, redirect, url_for, flash
from app import app
from app.db import cursor, db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author_first_name = request.form['author_first_name']
    author_last_name = request.form['author_last_name']
    read_status = int(request.form.get('read_status', 0))  # Convert to integer (1 for "Read", 0 for "Unread")
    isbn = request.form['isbn']
    description = request.form['description']
    image_url = request.form['image_url']
    external_url = request.form['external_url']
    media_id = int(request.form.get('media_id', 0))
    genre_id = int(request.form.get('genre_id', 0))

    if title and author_first_name and author_last_name and isbn and description and media_id:
        # Check if author already exists
        cursor.execute(
            "SELECT author_id FROM authors WHERE first_name = %s AND last_name = %s",
            (author_first_name, author_last_name)
        )
        author_data = cursor.fetchone()

        if not author_data:
            # If the author doesn't exist, insert into authors table
            cursor.execute(
                "INSERT INTO authors (first_name, last_name) VALUES (%s, %s)",
                (author_first_name, author_last_name)
            )
            db.commit()

            # Retrieve the newly inserted author's ID
            cursor.execute("SELECT LAST_INSERT_ID()")
            author_id = cursor.fetchone()[0]
        else:
            author_id = author_data[0]

        # Insert book into the database
        query = """
            INSERT INTO books 
            (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (title, author_id, read_status, isbn, description, image_url, external_url, media_id, genre_id)
        cursor.execute(query, values)
        db.commit()

        flash("Book added successfully!", "success")
    else:
        flash("Please fill in all required fields.", "warning")

    return redirect(url_for('index'))


@app.route('/display_books')
def display_books():
    # Retrieve books from the database with author information
    cursor.execute("""
            SELECT books.title, authors.first_name, authors.last_name, books.read_status, books.isbn, 
                   books.description, books.image_url, books.external_url, media.media_name, genres.genre_name
            FROM books 
            JOIN authors ON books.author_id = authors.author_id
            JOIN media ON books.media_id = media.media_id
            JOIN genres ON books.genre_id = genres.genre_id
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
