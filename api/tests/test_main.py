# File: api/tests/test_main.py
# File: api/tests/test_main.py
import os

import pytest
import yaml
from httpx import AsyncClient

from api.src.main import app


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
async def setup_test_env(test_config):
    # Check if API keys are set
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set in environment")
    if not os.getenv("GOOGLE_API_KEY"):
        pytest.skip("GOOGLE_API_KEY not set in environment")

    yield


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User API"}


@pytest.mark.asyncio
async def test_read_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_generate_response():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/generate_response", json={"text": "Tell me about AI"}
        )
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)
    assert len(response.json()["response"]) > 0


@pytest.mark.asyncio
async def test_missing_api_key(monkeypatch):
    # Temporarily remove the API key
    original_key = os.environ.get("OPENAI_API_KEY")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/generate_response", json={"text": "Tell me about AI"}
        )

    # Restore the original key
    if original_key:
        os.environ["OPENAI_API_KEY"] = original_key

    assert response.status_code == 500
    assert "Error initializing LLM service" in response.json()["detail"]


if __name__ == "__main__":
    pytest.main([__file__])
