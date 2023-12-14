from app import app
import mysql.connector
from dotenv import load_dotenv
import os
import secrets

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

    # Create medium table if not exists
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS medium (
                medium_id INT AUTO_INCREMENT PRIMARY KEY,
                medium_name VARCHAR(255) NOT NULL
            )
        """)
    db.commit()

    # Create genres table if not exists
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS genres (
                genre_id INT AUTO_INCREMENT PRIMARY KEY,
                genre_name VARCHAR(255) NOT NULL
            )
        """)
    db.commit()

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
            isbn VARCHAR(20),
            description TEXT,
            image_url VARCHAR(255),
            external_url VARCHAR(255),
            medium_id INT,
            genre_id INT,
            FOREIGN KEY (author_id) REFERENCES authors(author_id),
            FOREIGN KEY (medium_id) REFERENCES medium(medium_id),
            FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
        )
    """)
    db.commit()

except mysql.connector.Error as e:
    print(f"Error connecting to the database: {e}")


if __name__ == "__main__":
    app.run(debug=True)
