from locust import task, HttpUser
import random

class Swagger_load(HttpUser):
    token = None
    random.choice = None

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={
                'name': 'some_password'
            }
        )
        self.token = response.json()['token']


    @task(1)
    def get_all_memes(self):
        self.client.get(
            '/api/v3/user/',
            headers={
                'authorization': self.token
            }
        )


    @task(3)
    def get_one_meme(self):
        self.client.get(
            f'/api/v3/user/'{random.choice([1, 2, 3])},
            headers={
                'authorization': self.token
            }
        )
