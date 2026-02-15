import pytest
import requests
 

'''фикстуры используются от уровня их нахождения, приоритетнее будет фикстура описанная в самом исполняемом файле, потом на одном уровне с исполняемым 
файлом, в папке на уровень выше и так далее'''
import os 
import dotenv 



@pytest.fixture(scope='function')
def new_post_id():
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
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')