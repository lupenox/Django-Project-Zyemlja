from django.test import TestCase
from .models import MyUser

class AuthenticationTests(TestCase):
    def setUp(self):
        MyUser.objects.create(name="user1", password="pass1")

    def test_authenticate_user_valid(self):
        # Test that the authenticateUser correctly authenticates valid credentials
        user = authenticateUser("user1", "pass1")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "user1")

    def test_authenticate_user_invalid(self):
        # Test that the authenticateUser returns None for invalid credentials
        user = authenticateUser("user1", "wrongpass")
        self.assertIsNone(user)

class TATests(TestCase):
    def setUp(self):
        instructor = MyUser.objects.create(name="instructor", password="pass123")
        ta = MyUser.objects.create(name="ta1", password="pass123")
        course = Course.objects.create(name="Algebra", instructor=instructor)
        TeachingAssignment.objects.create(course=course, ta=ta)

    def test_get_ta_assignments(self):
        assignments = MyUser.getTAAssignments("ta1")
        self.assertEqual(len(assignments), 1)
        self.assertEqual(assignments[0].course.name, "Algebra")

    def test