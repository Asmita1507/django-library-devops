from django.test import TestCase
from .models import Book   # use relative import if needed

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(
            name="The Alchemist",
            author="Paulo Coelho",
            isbn=9780061122415,
            category="education"
        )

    def test_book_creation(self):
        book = Book.objects.get(name="The Alchemist")
        self.assertEqual(book.author, "Paulo Coelho")
        self.assertEqual(book.isbn, 9780061122415)
        self.assertEqual(book.category, "education")

    def test_string_representation(self):
        book = Book.objects.get(name="The Alchemist")
        expected_string = "The Alchemist[9780061122415]"
        self.assertEqual(str(book), expected_string)


