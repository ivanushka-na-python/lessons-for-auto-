import requests
import json

# хуйня где 5 != 5 

def create_post_for_put():
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
    
    return response.json()['id']


def put_post():
    post_id = create_post_for_put()
    print(post_id)

    body = {
        "title": "lol",
        "body": "ololololololo",
        "userId": 5
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/5', 
        json = body,
        headers = headers
        )

    res = response.json()
    print(res['id'], 'kutuyrurf')
    
    assert res['id'] is 5
    assert res['title'] == "lol"
    print(response.status_code)
    
updated_post = put_post()