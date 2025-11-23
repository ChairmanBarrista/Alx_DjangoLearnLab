from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookList(BookViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
