from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'testuser1',
            'email': 'testuser1@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser1').exists())
        
    def test_register_user2(self):
        response = self.client.post(self.register_url, self.user_data)
        self.user_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser2').exists())
