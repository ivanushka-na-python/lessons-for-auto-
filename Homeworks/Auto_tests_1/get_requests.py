import requests
import json

def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Not all posts returned'

get_all_posts()

# ------------------------------------------------------------------------------------------

def get_one_post(number_page):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{number_page}').json()
    assert response['id'] == number_page, 'Not this page' 

get_one_post(4)