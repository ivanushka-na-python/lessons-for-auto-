import requests
import pytest



def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/100')
