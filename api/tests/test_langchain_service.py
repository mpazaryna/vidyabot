# flake8: noqa: W293
import os

import pytest
import yaml

from api.src.langchain.langchain_service import get_langchain_service

# Correct path to config.yaml
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")

# Load the actual config.yaml
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


@pytest.fixture(scope="module", params=config["llm"]["options"])
def langchain_service(request):
    llm_type = request.param

    # Ensure API keys are set in the environment
    api_key_env = config[llm_type]["api_key_env"]
    if not os.getenv(api_key_env):
        pytest.skip(f"{api_key_env} not set in environment")

    # Temporarily modify the config for this test
    test_config = config.copy()
    test_config["llm"]["default"] = llm_type

    # Add 'model' key for Gemini if it's not present
    if llm_type == "gemini" and "model" not in test_config["gemini"]:
        test_config["gemini"][
            "model"
        ] = "gemini-pro"  # or whatever the correct model name is

    # Write the modified config to a temporary file
    test_config_path = "test_config.yaml"
    with open(test_config_path, "w") as file:
        yaml.dump(test_config, file)

    # Create and yield the service
    service = get_langchain_service(test_config_path)
    yield service

    # Clean up
    os.remove(test_config_path)


# ... [rest of the test functions remain the same]


def test_missing_api_key():
    # Temporarily remove API keys from environment
    api_keys = {}
    for llm_type in config["llm"]["options"]:
        api_key_env = config[llm_type]["api_key_env"]
        api_keys[api_key_env] = os.environ.pop(api_key_env, None)

    try:
        with pytest.raises(
            ValueError, match="API key not found in environment variable"
        ):
            get_langchain_service(CONFIG_PATH)
    finally:
        # Restore API keys
        for env, key in api_keys.items():
            if key:
                os.environ[env] = key


def test_unsupported_llm_type():
    # Create a temporary config with an unsupported LLM type
    test_config = config.copy()
    test_config["llm"]["default"] = "unsupported_llm"

    test_config_path = "test_unsupported_config.yaml"
    with open(test_config_path, "w") as file:
        yaml.dump(test_config, file)

    try:
        with pytest.raises(ValueError, match="Unsupported LLM type"):
            get_langchain_service(test_config_path)
    finally:
        # Clean up
        os.remove(test_config_path)
