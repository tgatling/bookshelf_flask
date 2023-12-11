class Book:
    def __init__(self, book_id, title, author_first_name, author_last_name, read_status, media, isbn, description,
                 image_url, external_url):
        self.book_id = book_id
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.read_status = read_status
        self.media = media
        self.isbn = isbn
        self.description = description
        self.image_url = image_url
        self.external_url = external_url
