import json
import os

# Load library from file if exists
def load_library(filename="library.txt"):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = file.read().strip()
                if data:  # Only parse if file is not empty
                    return json.loads(data)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not load data. Starting with an empty library.")
    return []

# Save library to file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    print("\nAdd a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_books(library):
    print("\nSearch for a Book")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search query: ").lower()
    matches = []

    if choice == "1":
        matches = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        matches = [book for book in library if query in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("\nMatching Books:")
        for idx, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    print("\nYour Library:")
    if not library:
        print("No books in the library.")
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_statistics(library):
    print("\nLibrary Statistics")
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_count = sum(1 for book in library if book["read"])
    percent_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main menu loop
def main():
    library = load_library()
    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
