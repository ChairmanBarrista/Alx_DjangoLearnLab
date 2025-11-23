from django.shortcuts import render

# Create your views here.
from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
