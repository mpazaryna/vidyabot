# File: api/tests/test_user_data.py

import json
from unittest.mock import mock_open, patch

import pytest

from api.src.data.user_data import get_user_data

MOCK_USER_DATA = {
    "users": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "age": 30,
            "city": "New York",
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "email": "bob.smith@example.com",
            "age": 25,
            "city": "San Francisco",
        },
    ]
}


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_USER_DATA))
def test_get_user_data(mock_file):
    users = get_user_data()
    assert users == MOCK_USER_DATA["users"]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    with pytest.raises(Exception, match="Error: The file .* was not found."):
        get_user_data()


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_invalid_json(mock_file):
    with pytest.raises(Exception, match="Error: The file .* contains invalid JSON."):
        get_user_data()


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"data": []}))
def test_missing_users_key(mock_file):
    with pytest.raises(
        Exception, match="Error: The 'users' key is missing in the JSON data."
    ):
        get_user_data()
