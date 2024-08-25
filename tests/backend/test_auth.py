import unittest
from unittest.mock import patch, MagicMock
from backend.auth import authenticate, login_user, logout_user

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.user = MagicMock(spec=User)
        self.user.username = 'testuser'
        self.user.password = 'password'

    def test_authenticate(self):
        self.user.check_password.return_value = True
        self.assertTrue(authenticate(self.user.username, self.user.password))
        self.user.check_password.assert_called_once_with(self.user.password)

    def test_authenticate_invalid_password(self):
        self.user.check_password.return_value = False
        self.assertFalse(authenticate(self.user.username, 'wrongpassword'))
        self.user.check_password.assert_called_once_with('wrongpassword')

    @patch('backend.auth.login_manager')
    def test_login_user(self, mock_login_manager):
        login_user(self.user)
        mock_login_manager.login_user.assert_called_once_with(self.user)

    @patch('backend.auth.login_manager')
    def test_logout_user(self, mock_login_manager):
        logout_user()
        mock_login_manager.logout_user.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
