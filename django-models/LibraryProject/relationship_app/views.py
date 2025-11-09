from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-Based View (FBV) — List All Books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    # Using namespaced template path
    return render(request, 'relationship_app/list_books.html', context)


# Class-Based View (CBV) — Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
