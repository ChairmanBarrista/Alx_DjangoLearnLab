from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test suite for CRUD, filtering, searching, ordering,
    and permission enforcement on Book API endpoints.
    """

    def setUp(self):
        # Create user and authenticate
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create author
        self.author = Author.objects.create(name="George Orwell")

        # Create initial book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})
        self.viewset_list_url = "/api/books_all/"  # router-generated
        self.viewset_detail_url = f"/api/books_all/{self.book.id}/"

    # ---------------------------
    # CRUD TESTS
    # ---------------------------

    def test_list_books(self):
        """Ensure the API can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        """Ensure a single book can be retrieved."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book(self):
        """Ensure a book can be created through the API."""
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }
        response = self.client.post(self.viewset_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Ensure an existing book can be updated."""
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(self.viewset_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        """Ensure a book can be deleted."""
        response = self.client.delete(self.viewset_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------------------------
    # AUTHENTICATION TESTS
    # ---------------------------

    def test_unauthenticated_user_cannot_create_book(self):
        """Ensure unauthenticated users are rejected."""
        client = APIClient()  # no login
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = client.post(self.viewset_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # FILTERING TESTS
    # ---------------------------

    def test_filter_books_by_title(self):
        """Ensure filtering by title works."""
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_filter_books_by_publication_year(self):
        """Ensure filtering by publication year works."""
        response = self.client.get(f"{self.list_url}?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1949)

    # ---------------------------
    # SEARCH TESTS
    # ---------------------------

    def test_search_books(self):
        """Ensure searching by title works."""
        response = self.client.get(f"{self.list_url}?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")

    # ---------------------------
    # ORDERING TESTS
    # ---------------------------

    def test_order_books_by_publication_year(self):
        """Ensure ordering by year works."""
        # Add newer book
        Book.objects.create(
            title="New Book",
            publication_year=2022,
            author=self.author
        )
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years))
