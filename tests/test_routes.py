import unittest
from app import app

class AgatuWebsiteTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client and set application to testing mode."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_administrations_route(self):
        response = self.client.get('/administrations')
        self.assertEqual(response.status_code, 200)

    def test_wards_route(self):
        response = self.client.get('/wards')
        self.assertEqual(response.status_code, 200)

    def test_projects_route(self):
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)

    def test_contact_route(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_departments_route(self):
        response = self.client.get('/departments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Secretariat Administrative Departments', response.data)
        self.assertIn(b'Local Government Education Authority', response.data)

    def test_404_page(self):
        response = self.client.get('/non-existent-route-12345')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()