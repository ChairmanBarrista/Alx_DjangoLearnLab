from django.db import models

# Create your models here.
# Author model: One-to-Many relationship with Book
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model: ForeignKey to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


# Library model: Many-to-Many relationship with Book
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# Librarian model: One-to-One relationship with Library
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name
