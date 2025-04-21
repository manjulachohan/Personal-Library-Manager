import json
import os

# File name for saving/loading library
data_file = 'library.txt'

# Load library if file exists
def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return []

# Save library to file
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

# Add a book
def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = ('Enter the genre of the book: ')
    read = input('Have you read this book? (yes/no): ').lower() == 'yes'
   
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(f'Book {title} added successfully!')

# Remove a book
def remove_book(library):
    title = input('Enter the title of the book to remove from the library: ')
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:    
        save_library(library)
        print(f'Book {title} removed successfully!')
            
    else:  
        print(f'Book {title} not found in the libraray. ')

# Search for a book
def search_library(library):
    search_by = input('Search by title or author').lower()
    search_term = input(f'Enter the {search_by} ').lower()
    
    results = [ book for book in library if search_term in book[search_by].lower()]
    
    if results:   
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - ({book['year']}) - {book['genre']} - {status}")
    else:
         print(f"No books found matching '{search_term}' in the {search_by} field.")
         
# Display all books
def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - ({book['year']}) - {book['genre']} - {status}")
    else:
        print("The library is empty.")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = len(book for book in library if book['read'])
    percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read : {percentage:.2f}%")

# Main menu
def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
