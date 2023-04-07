from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("index-page"))
        expected_data = "Hello"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response['name'], 'alex')  
        
    def test_contacts(self):
        response = self.client.get(reverse("contacts-view"))
        expected_data = "number"
        self.assertEqual(expected_data, response.content.decode())

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        expected_data = "about"
        self.assertEqual(expected_data, response.content.decode())
