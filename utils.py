
import json
from models import Book

BOOKS_FILE = 'books.json'

def load_books():
    try:
        with open(BOOKS_FILE, 'r') as file:
            data = json.load(file)
            return [Book(**book) for book in data]
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump([book.__dict__ for book in books], file, indent=4)
