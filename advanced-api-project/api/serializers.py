from rest_framework import serializers
from datetime import date
from .models import Book, Author

# BookSerializer is responsible for serializing all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year to ensure it is not in the future
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer is responsible for serializing the Author model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

