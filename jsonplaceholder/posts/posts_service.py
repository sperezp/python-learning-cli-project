import requests


def get_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    return r.json()
