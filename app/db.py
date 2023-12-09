import os

from flask import Flask
import os
import mysql.connector
from dotenv import load_dotenv
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

load_dotenv()

try:
    # Connect to MySQL database
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
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
