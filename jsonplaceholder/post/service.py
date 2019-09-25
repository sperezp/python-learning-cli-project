import requests

from jsonplaceholder.services import ServiceBase

API_URL = 'https://jsonplaceholder.typicode.com/posts'


class PostService(ServiceBase):
    def get_all(self):
        response = requests.get(API_URL)
        if response.ok:
            return response.json()
        return None
