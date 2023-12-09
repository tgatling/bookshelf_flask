-- Create the 'bookshelf' database
CREATE DATABASE IF NOT EXISTS bookshelf;

-- Switch to the 'bookshelf' database
USE bookshelf;

-- Create 'books' table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author_first_name VARCHAR(255),
    author_last_name VARCHAR(255),
    read_status BOOLEAN,
    media VARCHAR(20)
);

-- Create 'authors' table
CREATE TABLE IF NOT EXISTS authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
