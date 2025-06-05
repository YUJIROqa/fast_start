import unittest
import requests
import sys

class PostApi(unittest.TestCase):

    def setUp(self) -> None:
        body = {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    def tearDown(self) -> None:
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')

    @unittest.skip('Skipping test_get_one_post')
    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        self.assertEqual(response.json()['id'], self.post_id)


class TestIndependent(unittest.TestCase):

    @unittest.skipIf(sys.platform == 'darwin', 'Does not run on Linux')
    def test_get_all_posts(self):   
        response = requests.get('https://jsonplaceholder.typicode.com/posts')   
        self.assertEqual(len(response.json()), 100, 'Not all posts returned')

    def test_add_post(self):
        body = {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)

 
#1.04

        