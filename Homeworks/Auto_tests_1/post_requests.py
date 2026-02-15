import requests

def create_post():
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
    assert response.status_code == 201, 'error'
    assert response.json()['id'] == 101
    print(response.json())
    
create_post()