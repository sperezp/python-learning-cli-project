import requests

from jsonplaceholder.services import ServiceBase


class PostService(ServiceBase):
    def get_all(self):
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        return r.json()
