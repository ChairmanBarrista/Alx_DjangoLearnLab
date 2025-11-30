from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
# Serializes book data. Including validation to prevent future publication years.

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


class AuthorSerializer(serializers.ModelSerializer):
# Serializes authors AND their related books. Using nested BookSerializer to show full book details.

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
