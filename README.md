# Bookshelf

## Overview

Bookshelf is a simple web application built with Flask for tracking and managing your book collection.
It allows you to add books, mark their read status, and view the collection.

## Current Features

- Add books to your collection
- Mark books as read or unread
- View your book collection

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11.5
- Flask 3.0.0
- MySQL database

### Project Structure

The project follows a specific structure to organize its components. Here is an overview:

- `app.py`: The main application file.
- `database/`: Includes database schema and setup scripts
    - `schema.sql`: SQL script for the database schema.
- `templates/`: Contains HTML templates.
- `static/`: Contains static files such as CSS.

### Installation

Follow these steps to set up and run the application

#### Clone Repository

   ```bash
  git remote add origin https://github.com/tgatling/bookshelf_flask.git
   ```

#### Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

#### Setup MySQL Database

- Create a MySQL database and update the database configuration in `config.py`
- Run the database setup script:
    ```bash
    python database/setup.py
    ```

#### Configure Environmental Variables

- Copy the `.env.example` file to a new file named `.env`
- Replace the placeholder values with your actual configuration.

#### Run Application

   ```bash
   python run.py
   ```

#### Web Browser

Open your web browser and go to http://localhost:5000.

## Testing

### Running Tests

1. Ensure that you have PyTest installed. If not, install using:
    ```bash
    pip install pytest
    ```
2. Navigate to the project's root directory in the terminal.
3. Run the PyTest command to discover and run tests:
    ```bash
    pytest
    ```
   PyTest will automatically discover and execute all test files that match the naming pattern
   `test_*` or `*_test.py` in the project.

## Future Enhancements

- View book detail page with additional information
- Edit and remove books from collection
- Search implementation
- Data validation

## Acknowledgements

- Flask: Web Framework for Python
- Jinja2: Template engine for Python
