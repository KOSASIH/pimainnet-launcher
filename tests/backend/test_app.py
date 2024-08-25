import unittest
from unittest.mock import patch, MagicMock
from backend.app import create_app
from backend.models import User

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to our app!', response.data)

    def test_user_registration(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password'}
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful!', response.data)
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)

    @patch('backend.auth.login_user')
    def test_login(self, mock_login_user):
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post('/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful!', response.data)
        mock_login_user.assert_called_once_with(User.query.filter_by(username='testuser').first())

    def test_logout(self):
        with self.client.session_transaction() as sess:
            sess['user_id'] = 1
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logout successful!', response.data)
        self.assertNotIn('user_id', self.client.session)

if __name__ == '__main__':
    unittest.main()
