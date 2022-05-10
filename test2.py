import unittest
from app import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # Tester la page d'accueil
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        
    # Tester la page de contact
    def test_contact(self):
        rv = self.app.get('/contact')
        self.assertEqual(rv.status, '200 OK')

    # Tester la page a propos
    def test_a_propos(self):
        rv = self.app.get('/a-propos')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
