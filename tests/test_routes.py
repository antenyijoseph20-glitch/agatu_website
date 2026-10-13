import os
import unittest

# Ensure secret key is set for testing session
os.environ["FLASK_SECRET_KEY"] = "test-secret-key"

from app import app

class AgatuWebsiteTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_projects_route(self):
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)

    def test_project_detail_route(self):
        response = self.app.get('/project/1')
        self.assertEqual(response.status_code, 200)

    def test_wards_route(self):
        response = self.app.get('/wards')
        self.assertEqual(response.status_code, 200)

    def test_contact_route(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
    
    def test_administrations_route(self):
        response = self.app.get('/administrations')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()