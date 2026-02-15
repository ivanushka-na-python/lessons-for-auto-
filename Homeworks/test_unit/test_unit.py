import unittest
import requests


class TestPostAPI(unittest.TestCase):

    # def test_get_all_post(self):
    #     response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    #     self.assertEqual(len(response), 100)


    def test_add_post(self):
        body = {
            "title": "еуыеуеыуе",
            "body": "hello",
            "userId": 1
        }
        headers = {'Content-Type': 'aplication/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', 
        json = body,
        headers = headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)