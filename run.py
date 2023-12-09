from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

try:
    load_dotenv()

    # Connect to MySQL database
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = db.cursor()

    # Create authors table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        )
    """)
    db.commit()

    # Create books table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author_id INT,
            read_status BOOLEAN,
            media VARCHAR(20),
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        )
    """)
    db.commit()

except mysql.connector.Error as e:
    print(f"Error connecting to the database: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author_first_name = request.form['author_first_name']
    author_last_name = request.form['author_last_name']
    read_status = int(request.form.get('read_status', 0))  # Convert to integer (1 for "Read", 0 for "Unread")
    media = request.form['media']

    if title and author_first_name and author_last_name:
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
            (title, author_id, read_status, media) 
            VALUES (%s, %s, %s, %s)
        """
        values = (title, author_id, read_status, media)
        cursor.execute(query, values)
        db.commit()

        flash("Book added successfully!", "success")
    else:
        flash("Please fill in title and author fields.", "warning")

    return redirect(url_for('index'))


@app.route('/display_books')
def display_books():
    # Retrieve books from the database with author information
    cursor.execute("""
        SELECT books.title, authors.first_name, authors.last_name, books.read_status, books.media 
        FROM books 
        JOIN authors ON books.author_id = authors.author_id
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
