import sys
from book_manager import add_book, list_books, remove_book

def print_usage():
    print("Usage:")
    print("  add <title> <author>    Add a new book")
    print("  list                    List all books")
    print("  remove <title>           Remove a book")
    print("  help                    Show this help message")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Error: 'add' command requires title and author")
            print_usage()
            return
        title = sys.argv[2]
        author = sys.argv[3]
        add_book(title, author)
    elif command == "list":
        list_books()
    elif command == "remove":
        if len(sys.argv) != 3:
            print("Error: 'remove' command requires title")
            print_usage()
            return
        title = sys.argv[2]
        remove_book(title)
    elif command == "help":
        print_usage()
    else:
        print("Unknown command")
        print_usage()

if __name__ == '__main__':
    main()
