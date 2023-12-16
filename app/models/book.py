class Book:
    def __init__(self, title, author_id, read_status, isbn, description,
                 image_url, external_url, medium_id, genre_id):
        self.book_id = None
        self.title = title
        self.author_id = author_id
        self.read_status = read_status
        self.isbn = isbn
        self.description = description
        self.image_url = image_url
        self.external_url = external_url
        self.medium_id = medium_id
        self.genre_id = genre_id

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, " \
               f"Author ID: {self.author_id}, Read Status: {'Read' if self.read_status else 'Unread'}, " \
               f"Medium ID: {self.medium_id}, Genre ID: {self.genre_id}"


class DisplayBooksResponseItem:
    def __init__(self, book_id, title, author_first_name, author_last_name, read_status, medium, isbn, description,
                 image_url, external_url, genre):
        self.book_id = book_id
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.read_status = read_status
        self.medium = medium
        self.isbn = isbn
        self.description = description
        self.image_url = image_url
        self.external_url = external_url
        self.genre = genre

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, " \
               f"Author: {self.author_first_name} {self.author_last_name}, " \
               f"Read Status: {'Read' if self.read_status else 'Unread'}, Medium: {self.medium}, Genre: {self.genre}"
