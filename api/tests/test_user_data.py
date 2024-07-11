# File: api/tests/test_user_data.py

import json
import os

import pytest

from api.src.data.user_data import get_user_data


@pytest.fixture
def sample_data():
    return {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com",
                "age": 30,
                "city": "New York",
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com",
                "age": 25,
                "city": "San Francisco",
            },
        ]
    }


@pytest.fixture
def setup_test_file(tmp_path, sample_data):
    # Create a temporary directory structure
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    data_dir = api_dir / "static_data"
    data_dir.mkdir()
    test_file = data_dir / "user_data.json"

    # Write sample data to the test file
    with open(test_file, "w") as f:
        json.dump(sample_data, f)

    # Return the path to the test file
    return test_file


def test_get_user_data(monkeypatch, setup_test_file, sample_data):
    # Patch the os.path.dirname to return our temporary directory
    monkeypatch.setattr(
        os.path, "dirname", lambda x: str(setup_test_file.parent.parent)
    )

    # Call the function
    result = get_user_data()

    # Check if the result matches our sample data
    assert result == sample_data["users"]


def test_file_not_found(monkeypatch, tmp_path):
    # Patch the os.path.dirname to return a directory without the file
    monkeypatch.setattr(os.path, "dirname", lambda x: str(tmp_path))

    # Call the function
    result = get_user_data()

    # Check if the result is an empty list
    assert result == []


def test_invalid_json(monkeypatch, tmp_path):
    # Create an invalid JSON file
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    data_dir = api_dir / "static_data"
    data_dir.mkdir()
    test_file = data_dir / "user_data.json"
    test_file.write_text("{ invalid json }")

    # Patch the os.path.dirname to return our temporary directory
    monkeypatch.setattr(os.path, "dirname", lambda x: str(api_dir))

    # Call the function
    result = get_user_data()

    # Check if the result is an empty list
    assert result == []


def test_missing_users_key(monkeypatch, tmp_path):
    # Create a JSON file without a 'users' key
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    data_dir = api_dir / "static_data"
    data_dir.mkdir()
    test_file = data_dir / "user_data.json"
    test_file.write_text('{"data": []}')

    # Patch the os.path.dirname to return our temporary directory
    monkeypatch.setattr(os.path, "dirname", lambda x: str(api_dir))

    # Call the function
    result = get_user_data()

    # Check if the result is an empty list
    assert result == []


def test_docstring_presence():
    """Test that the get_user_data function has a docstring."""
    assert (
        get_user_data.__doc__ is not None
    ), "get_user_data function is missing a docstring"
