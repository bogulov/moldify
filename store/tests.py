from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class IndexViewTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_view_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')