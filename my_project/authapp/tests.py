from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token


class AccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.update_profile_url = reverse('update_profile')
        self.delete_account_url = reverse('delete_account')

    def test_register_new_user(self):
        response = self.client.post(
            self.registration_url,
            {'username': 'testuser', 'email': 'test@test.com', 'password': 'securepass'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_register_existing_email(self):
        existing_user = User.objects.create_user(username="existing", email="exist@mail.ru")
        response = self.client.post(
            self.registration_url,
            {'username': 'newuser', 'email': 'exist@mail.ru', 'password': 'anotherpass'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_successfully(self):
        user = User.objects.create_user(username="validuser", email="valid@user.com", password="rightpass")
        response = self.client.post(
            self.login_url,
            {'username': 'validuser', 'password': 'rightpass'}
        )

