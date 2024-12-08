from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """BookSerializer is responsible for serializing the Book model."""
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, data):
        """Custom validation for publication_year to ensure it is not in the future"""
        if data > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """AuthorSerializer is responsible for serializing the Author model."""
    books = BookSerializer(many=True, read_only = True)

    class Meta:
        model = Author
        fields = ['name', 'books']