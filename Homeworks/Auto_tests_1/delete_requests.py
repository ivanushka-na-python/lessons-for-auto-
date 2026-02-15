import requests

def delete_post(post_number):
    response = requests.delete('https://jsonplaceholder.typicode.com/posts' + post_number).status_code
    print(response)

delete_post('/1')
