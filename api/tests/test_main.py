# File: api/tests/test_main.py

import json
from unittest.mock import mock_open, patch

import pytest
from fastapi.testclient import TestClient

from api.src.main import app

client = TestClient(app)

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


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User API"}


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_USER_DATA))
def test_read_users(mock_file):
    """Test the /users endpoint."""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == MOCK_USER_DATA["users"]


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"users": []}))
def test_read_users_empty(mock_file):
    """Test the /users endpoint when no users are returned."""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


@patch("builtins.open", side_effect=Exception("Test error"))
def test_read_users_error(mock_file):
    """Test error handling in the /users endpoint."""
    response = client.get("/users")
    assert response.status_code == 500
    assert response.json() == {"detail": "An unexpected error occurred: Test error"}


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("/docs", 200),
        ("/openapi.json", 200),
        ("/nonexistent", 404),
    ],
)
def test_other_routes(test_input, expected):
    """Test other routes including auto-generated docs and nonexistent routes."""
    response = client.get(test_input)
    assert response.status_code == expected
