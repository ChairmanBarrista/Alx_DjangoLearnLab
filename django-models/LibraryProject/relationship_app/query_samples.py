from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")


# 2️⃣ List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name} Library:")
    for book in books:
        print(f"- {book.title}")


# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    Library.objects.get(name=library_name) = library
    ibrary.librarian = librarian
    print(f"Librarian for {library.name} Library: {librarian.name}")


# Example function calls (for testing in Django shell)
if __name__ == "__main__":
    get_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
