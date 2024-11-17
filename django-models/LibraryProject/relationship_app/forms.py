from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date', 'isbn_number']  # Fields you want to include in the form
