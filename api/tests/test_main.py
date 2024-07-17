# File: api/tests/test_main.py
import os

import pytest
import yaml
from fastapi.testclient import TestClient

from api.src.main import app, get_cached_langchain_service

client = TestClient(app)


@pytest.fixture(scope="module")
def test_config():
    # Create a test configuration
    config = {
        "llm": {"default": "openai", "options": ["openai", "gemini"]},
        "openai": {"api_key_env": "OPENAI_API_KEY"},
        "gemini": {"api_key_env": "GOOGLE_API_KEY"},
    }

    # Write the test configuration to a file
    with open("test_config.yaml", "w") as file:
        yaml.dump(config, file)

    yield "test_config.yaml"

    # Clean up
    os.remove("test_config.yaml")


@pytest.fixture(autouse=True)
def setup_test_env(test_config):
    # Clear the lru_cache for get_cached_langchain_service
    get_cached_langchain_service.cache_clear()

    # Check if API keys are set
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set in environment")
    if not os.getenv("GOOGLE_API_KEY"):
        pytest.skip("GOOGLE_API_KEY not set in environment")

    yield

    # Clear the cache again after the test
    get_cached_langchain_service.cache_clear()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User API"}


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_generate_response():
    response = client.post("/generate_response", json={"text": "Tell me about AI"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)
    assert len(response.json()["response"]) > 0


def test_missing_api_key(monkeypatch):
    # Temporarily remove the API key
    original_key = os.environ.get("OPENAI_API_KEY")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    get_cached_langchain_service.cache_clear()

    response = client.post("/generate_response", json={"text": "Tell me about AI"})

    # Restore the original key
    if original_key:
        os.environ["OPENAI_API_KEY"] = original_key
    get_cached_langchain_service.cache_clear()

    assert response.status_code == 500
    assert "Error initializing LLM service" in response.json()["detail"]


if __name__ == "__main__":
    pytest.main([__file__])
