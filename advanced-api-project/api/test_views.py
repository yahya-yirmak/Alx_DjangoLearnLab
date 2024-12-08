from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Log in the user
        self.client.login(username="testuser", password="testpass")
        # Create test data
        self.book1 = Book.objects.create(title="Test Book 1", author="Author 1", publication_year=2020)
        self.book2 = Book.objects.create(title="Test Book 2", author="Author 2", publication_year=2021)
        self.list_url = reverse('book-list')  # Replace 'book-list' with your endpoint


    def test_list_books(self):
        # Test retrieving the list of books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book
        data = {"title": "New Book", "author": "New Author", "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        # Test updating an existing book
        update_url = reverse('book-detail', args=[self.book1.id])  # Replace 'book-detail' with your endpoint
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2023}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        # Test deleting a book
        delete_url = reverse('book-detail', args=[self.book1.id])  # Replace 'book-detail' with your endpoint
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        # Test filtering books by title
        response = self.client.get(self.list_url, {'title__icontains': 'Test Book 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_search_books(self):
        # Test searching books
        response = self.client.get(self.list_url, {'search': 'Author 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 2')

    def test_order_books(self):
        # Test ordering books by publication year
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)
