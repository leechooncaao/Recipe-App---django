from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test creating user"""
        email = 'leechoncaao@gmail.com'
        password = 'Ahihi123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of a new user is normalized"""
        email = 'leechoncaao@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1233')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'superuser@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
