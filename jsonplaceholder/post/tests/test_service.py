from unittest.mock import patch

import pytest

from jsonplaceholder.post.service import PostService


@patch('jsonplaceholder.post.service.requests')
def test_get_all_success(requests):
    requests.get.return_value.ok = True
    response = PostService().get_all()
    assert response is not None


@patch('jsonplaceholder.post.service.requests')
def test_get_all_fail(requests):
    requests.get.return_value.ok = False
    response = PostService().get_all()
    assert response is None


@patch('jsonplaceholder.post.service.requests')
def test_get_all_timeout(requests):
    requests.get.side_effect = TimeoutError

    with pytest.raises(TimeoutError):
        PostService().get_all()
