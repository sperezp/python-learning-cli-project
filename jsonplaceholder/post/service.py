import requests

from jsonplaceholder.services import ServiceBase


class PostService(ServiceBase):
    def get_all(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return response.json()
