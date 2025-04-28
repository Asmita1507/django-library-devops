from django.test import TestCase
from django.contrib.auth.models import User
from library.models import Book, StudentExtra

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name="Simple Book",
            author="Simple Author",
            isbn="1234567890123"
        )

    def test_book_creation(self):
        """Test that a Book object is created with correct attributes."""
        self.assertEqual(self.book.name, "Simple Book")
        self.assertEqual(self.book.author, "Simple Author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_str(self):
        """Test that the string representation of a Book is its name and isbn."""
        self.assertEqual(str(self.book), "Simple Book[1234567890123]")

class StudentExtraModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student', password='testpass')
        self.student = StudentExtra.objects.create(
            user=self.user,
            enrollment="12345",
            branch="CS"
        )

    def test_student_creation(self):
        """Test that a StudentExtra object is created with correct attributes."""
        self.assertEqual(self.student.enrollment, "12345")
        self.assertEqual(self.student.branch, "CS")
        self.assertEqual(self.student.user.username, "student")
