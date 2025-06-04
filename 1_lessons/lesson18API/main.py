import requests # библиотека для отправки запросов
import json

def all_posts():
    req = requests.get('https://jsonplaceholder.typicode.com/posts') # отправляем запрос на сервер
    print(req.json()[0]) # выводим ответ сервера
    print('='*100)
    assert len(req.json()) == 100, 'Количество постов не соответствует 100'

def one_post():
    post_id = 42
    req = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}') # отправляем запрос на сервер
    print(req.json()) # выводим ответ сервера
    assert req.json()['id'] == post_id, 'id поста не соответствует 42'
    print('='*100)

def post_a_post(): # отправляем пост на сервер
    body = {
        'title': 'food',  # заголовок поста
        'body': 'mybody', # тело поста
        'userId': 1       # id пользователя
    }
    headers = {
        'Content-Type': 'application/json'
    }
    req = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    print(req.json())
    print(req.status_code)
    print('='*100)

def put_a_post(): # отправляем пост на сервер
    body = {
        'title': 'food',  # заголовок поста
        'body': 'mybody', # тело поста
        'userId': 1       # id пользователя
    }
    headers = {
        'Content-Type': 'application/json'
    }
    req = requests.put('https://jsonplaceholder.typicode.com/posts/42', json=body, headers=headers)
    print(req.json())
    print('='*100)

def delete_a_post(): # удаляем пост на сервер
    req = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(req.json())
    print(req.status_code)
    print('='*100)

all_posts()
one_post()
post_a_post()
put_a_post()
delete_a_post()
