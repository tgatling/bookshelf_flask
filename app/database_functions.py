from app.db import cursor


def get_author_id(author_first_name, author_last_name):
    query = "SELECT author_id FROM authors WHERE first_name = %s AND last_name = %s"
    cursor.execute(query, (author_first_name, author_last_name))
    result = cursor.fetchone()
    author_id = result[0] if result else None
    return author_id


def get_genre_id(genre_name):
    query = "SELECT genre_id FROM genres WHERE genre_name = %s"
    cursor.execute(query, (genre_name,))
    result = cursor.fetchone()
    genre_id = result[0] if result else None
    return genre_id


def get_media_id(media_name):
    query = "SELECT media_id FROM media WHERE media_name = %s"
    cursor.execute(query, (media_name,))
    result = cursor.fetchone()
    media_id = result[0] if result else None
    return media_id
