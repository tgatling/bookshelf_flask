-- Create the 'bookshelf' database
CREATE DATABASE IF NOT EXISTS bookshelf;

-- Use the 'bookshelf' database
USE bookshelf;

-- Create the 'media' table
CREATE TABLE IF NOT EXISTS media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    media_name VARCHAR(255) NOT NULL
);

-- Create the 'genre' table
CREATE TABLE IF NOT EXISTS genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

-- Create the 'authors' table
CREATE TABLE IF NOT EXISTS authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- Create the 'books' table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    read_status BOOLEAN,
    isbn VARCHAR(20),
    description TEXT,
    image_url VARCHAR(255),
    external_url VARCHAR(255),
    media_id INT,
    genre_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (media_id) REFERENCES media(media_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);
