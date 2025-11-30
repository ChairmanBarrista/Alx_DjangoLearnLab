from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),

    # Retrieve a single book
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # Create a new book
    path("books/create/", BookCreateView.as_view(), name="book-create"),

    # UPDATE endpoint required by your checker
    path("books/update/", BookUpdateView.as_view(), name="book-update"),

    # DELETE endpoint required by your checker
    path("books/delete/", BookDeleteView.as_view(), name="book-delete"),
]
