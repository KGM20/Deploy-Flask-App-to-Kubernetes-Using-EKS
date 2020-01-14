'''
Tests for jwt flask app.
'''
import os
import json
import unittest
from unittest.mock import patch

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjEzMDY3OTAsIm5iZiI6MTU2MDA5NzE5MCwiZW1haWwiOiJ3b2xmQHRoZWRvb3IuY29tIn0.IpM4VMnqIgOoQeJxUbLT-cRcAjK41jronkVrqRLFmmk'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):

        self.app = main.APP
        self.client = self.app.test_client
        self.env = patch.dict('os.environ', {'JWT_SECRET':SECRET})
        self.user = {
                        'email': EMAIL,
                        'password': PASSWORD
                    }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_health(self):
        res = self.client().get('/')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, 'Healthy')

    def test_auth(self):
        res = self.client().post('/auth', json=self.user)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['token'])

if __name__ == "__main__":
    unittest.main()