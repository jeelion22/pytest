import pytest

import source.service as servic
import unittest.mock as mock
import requests


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = servic.get_user_from_db(1)

    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = servic.get_users()

    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(moke_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400

    moke_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        servic.get_users()
