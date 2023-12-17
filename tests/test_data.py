from app.models import Book, Author, Genre, Medium, DisplayBooksResponseItem

test_book_id = 1
test_title = "Test Title"
test_read_status = 1
test_isbn = 1234567890
test_description = "This is a test book description"
test_image_url = "https://example.com/image.jpg"
test_external_url = "https://example.com/"
test_author_id = 1
test_genre_id = 1
test_medium_id = 1

test_author_first_name = "Test"
test_author_last_name = "Author"
test_author_full_name = "Test Author"
test_genre_name = "Programming"
test_medium_name_ebook = "Ebook"
test_medium_name_audiobook = "Audiobook"
test_medium_name_physical = "Physical"

test_author = Author(test_author_first_name, test_author_last_name)
test_genre = Genre(test_genre_name)
test_medium = Medium(test_medium_name_audiobook)
test_medium.medium_id = test_medium_id

test_ebook = Book(test_title, test_read_status, test_isbn, test_description, test_image_url, test_external_url,
                  test_author_id, test_genre_id, test_medium_id)

test_display_ebook = DisplayBooksResponseItem(test_book_id, test_title, test_author_first_name,
                                              test_author_last_name, test_read_status, test_medium_name_ebook,
                                              test_isbn, test_description, test_image_url,
                                              test_external_url, test_genre_name)

test_display_physical_book = DisplayBooksResponseItem(test_book_id, test_title, test_author_first_name,
                                                      test_author_last_name, test_read_status,
                                                      test_medium_name_physical, test_isbn, test_description,
                                                      test_image_url, test_external_url, test_genre_name)

test_display_audiobook = DisplayBooksResponseItem(test_book_id, test_title, test_author_first_name,
                                                  test_author_last_name, test_read_status,
                                                  test_medium_name_audiobook, test_isbn, test_description,
                                                  test_image_url, test_external_url, test_genre_name)


