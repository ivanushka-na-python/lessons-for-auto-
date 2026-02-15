import unittest
import requests


class TestGetAPI(unittest.TestCase):

    def setUp(self): # предусловия 
        body = {
            "title": "Hi",
            "body": "Hello",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts', 
            json = body,
            headers = headers
            ) 
        self.post_id = response.json()['id']

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')

    @unittest.skip # @unittest.skipIf(sys.platform == 'dsrwin', 'not for mac os')
    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)


class TestPostGetAPI(unittest.TestCase):

    def test_get_all_post(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)


    def test_add_post(self):
        body = {
            "title": "еуыеуеыуе",
            "body": "hello",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', 
        json = body,
        headers = headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)

