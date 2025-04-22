from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
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

class LibraryViewTest(TestCase):
    def setUp(self):
        # Create an admin user
        self.user = User.objects.create_user(username='admin', password='testpass')
        admin_group, _ = Group.objects.get_or_create(name='ADMIN')
        self.user.groups.add(admin_group)
        
        # Log in the admin user
        self.client.login(username='admin', password='testpass')
        
        # Create test data
        self.book = Book.objects.create(
            name="Simple Book",
            author="Simple Author",
            isbn="1234567890123"
        )
        self.student_user = User.objects.create_user(username='student', password='testpass')
        self.student = StudentExtra.objects.create(
            user=self.student_user,
            enrollment="12345",
            branch="CS"
        )

    def test_viewbook_view(self):
        """Test that viewbook_view returns 200 and uses correct template for admin."""
        response = self.client.get(reverse('library:view_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/viewbook.html')

    def test_viewstudent_view(self):
        """Test that viewstudent_view returns 200 and uses correct template for admin."""
        response = self.client.get(reverse('library:view_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/viewstudent.html')
