import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {"title": "fsakj", "body": "baras", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    post_id = response.json()['id']
    print(f'Post created: {post_id}')
    yield post_id
    print('Deleting post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session')
def hello():
     print('hello')
     yield
     print('bye')


def test_get_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    assert response.json()['id'] == new_post_id


def test_get_all_posts(hello):   
    response = requests.get('https://jsonplaceholder.typicode.com/posts')   
    assert len(response.json()) == 100, 'Not all posts returned'


def test_add_post():
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
        assert response.status_code == 201
        assert response.json()['id'] == 101
 
@pytest.mark.regression
def test_one():
     assert 1 == 1

@pytest.mark.smoke
def test_two():
     assert 1 == 2

@pytest.mark.smoke
def test_three():
     assert 1 == 3

@pytest.mark.parametrize('logins', ['', '   ', '*%9*%34'])
def test_four(logins):
    print(logins)
    assert 1 == 1
