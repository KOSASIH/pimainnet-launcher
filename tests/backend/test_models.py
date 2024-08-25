import unittest
from backend.models import User, db

class TestModels(unittest.TestCase):
    def setUp(self):
        self.user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(self.user)
        db.session.commit()

    def test_user(self):
        self.assertIsNotNone(self.user.id)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_user_password_hashing(self):
        self.assertIsNotNone(self.user.password_hash)
        self.assertNotEqual(self.user.password_hash, 'password')

    def test_user_password_verification(self):
        self.assertTrue(self.user.check_password('password'))
        self.assertFalse(self.user.check_password('wrongpassword'))

if __name__ == '__main__':
    unittest.main()
