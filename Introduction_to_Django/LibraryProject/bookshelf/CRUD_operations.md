# CREATE
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>


#RETRIEVE
Book.objects.get(title="1984")
# Expected Output:
# <Book: 1984 by George Orwell (1949)>


# UPDATE
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>


#DELETE
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
