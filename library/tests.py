from django.test import TestCase
  from django.urls import reverse
  from library.models import Book, Borrower

  class BookModelTest(TestCase):
      def setUp(self):
          self.book = Book.objects.create(
              title="Simple Book",
              author="Simple Author",
              isbn="1234567890123",
              published_date="2023-01-01",
              genre="Fiction",
              available_copies=5,
              total_copies=5
          )

      def test_book_creation(self):
          """Test that a Book object is created with correct attributes."""
          self.assertEqual(self.book.title, "Simple Book")
          self.assertEqual(self.book.author, "Simple Author")
          self.assertEqual(self.book.available_copies, 5)

  class BorrowerModelTest(TestCase):
      def setUp(self):
          self.borrower = Borrower.objects.create(
              name="Jane Doe",
              email="jane@example.com",
              phone_number="1234567890",
              address="123 Main St"
          )

      def test_borrower_creation(self):
          """Test that a Borrower object is created with correct attributes."""
          self.assertEqual(self.borrower.name, "Jane Doe")
          self.assertEqual(self.borrower.email, "jane@example.com")

  class LibraryViewTest(TestCase):
      def setUp(self):
          self.book = Book.objects.create(
              title="Simple Book",
              author="Simple Author",
              isbn="1234567890123",
              published_date="2023-01-01",
              genre="Fiction",
              available_copies=5,
              total_copies=5
          )
          self.borrower = Borrower.objects.create(
              name="Jane Doe",
              email="jane@example.com",
              phone_number="1234567890",
              address="123 Main St"
          )

      def test_book_list_view(self):
          """Test that the book list view returns 200 and uses correct template."""
          response = self.client.get(reverse('book_list'))
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'library/book_list.html')

      def test_borrower_list_view(self):
          """Test that the borrower list view returns 200 and uses correct template."""
          response = self.client.get(reverse('borrower_list'))
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'library/borrower_list.html')
