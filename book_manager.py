from models import Book
from utils import load_books, save_books

def add_book(title, author):
    books = load_books()
    new_book = Book(title, author)
    books.append(new_book)
    save_books(books)
    print(f"Book added: {new_book}")

def list_books():
    books = load_books()
    if not books:
        print("No books found.")
    for book in books:
        print(book)

def remove_book(title):
    books = load_books()
    books = [book for book in books if book.title != title]
    save_books(books)
    print(f"Book '{title}' removed.")
