import json
from django.test import TestCase
from rest_framework.test import APIClient


class PasswordGeneratorTests(TestCase):
    def test_badrequest_api(self):
        client = APIClient()
        response = client.post('', data={})
        self.assertEqual(response.status_code, 400)

    def test_api(self):
        client = APIClient()
        response = client.post('', data={
            "min_length": 8,
            "special_char": 2,
            "number_of_numbers": 2,
            "number_of_passwords": 5
        })
        contents = json.loads(response.content)
        
        self.assertNotEqual(len(contents['passwords']), 0)
        self.assertEqual(len(contents['passwords']), 5)
        self.assertEqual(response.status_code, 200)
