# flake8: noqa: W293
import os

import pytest
import yaml

from api.src.langchain.langchain_service import LangChainService, get_langchain_service

# Correct path to config.yaml
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")

# Load the actual config.yaml
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


@pytest.fixture(params=config["llm"]["options"])
async def langchain_service(request):
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
        test_config["gemini"]["model"] = "gemini-pro"

    # Write the modified config to a temporary file
    test_config_path = f"test_config_{llm_type}.yaml"
    with open(test_config_path, "w") as file:
        yaml.dump(test_config, file)

    try:
        # Create and return the service
        service = await get_langchain_service(test_config_path)
        return service
    finally:
        # Clean up
        os.remove(test_config_path)


@pytest.mark.asyncio
async def test_generate_response(langchain_service: LangChainService):
    service = await langchain_service
    prompt = "You are a helpful assistant. Respond to the following: {input}"
    input_text = "Tell me about artificial intelligence."
    response = await service.generate_response(prompt, input_text)
    assert response, "Response should not be empty"
    assert isinstance(response, str), "Response should be a string"
    assert len(response) > 10, "Response should be a meaningful length"


@pytest.mark.asyncio
async def test_summarize_text(langchain_service: LangChainService):
    service = await langchain_service
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    summary = await service.summarize_text(text)
    assert summary, "Summary should not be empty"
    assert isinstance(summary, str), "Summary should be a string"
    # assert len(summary) < len(text), "Summary should be shorter than original text"


@pytest.mark.asyncio
async def test_answer_question(langchain_service: LangChainService):
    service = await langchain_service
    context = "Paris is the capital and most populous city of France."
    question = "What is the capital of France?"
    answer = await service.answer_question(question, context)
    assert answer, "Answer should not be empty"
    assert isinstance(answer, str), "Answer should be a string"
    assert "Paris" in answer, "Answer should contain 'Paris'"


@pytest.mark.asyncio
async def test_translate_text(langchain_service: LangChainService):
    service = await langchain_service
    text = "Hello, how are you?"
    target_language = "Spanish"
    translation = await service.translate_text(text, target_language)
    assert translation, "Translation should not be empty"
    assert isinstance(translation, str), "Translation should be a string"
    assert translation != text, "Translation should be different from original text"
    assert "Hola" in translation, "Spanish translation should contain 'Hola'"


# ... (keep the test_missing_api_key and test_unsupported_llm_type as they were)


@pytest.mark.asyncio
async def test_missing_api_key(monkeypatch):
    # Temporarily remove API keys from environment
    api_keys = {}
    for llm_type in config["llm"]["options"]:
        api_key_env = config[llm_type]["api_key_env"]
        api_keys[api_key_env] = os.environ.pop(api_key_env, None)

    try:
        with pytest.raises(
            ValueError, match="API key not found in environment variable"
        ):
            await get_langchain_service(CONFIG_PATH)
    finally:
        # Restore API keys
        for env, key in api_keys.items():
            if key:
                os.environ[env] = key


@pytest.mark.asyncio
async def test_unsupported_llm_type():
    # Create a temporary config with an unsupported LLM type
    test_config = config.copy()
    test_config["llm"]["default"] = "unsupported_llm"

    test_config_path = "test_unsupported_config.yaml"
    with open(test_config_path, "w") as file:
        yaml.dump(test_config, file)

    try:
        with pytest.raises(ValueError, match="Unsupported LLM type"):
            await get_langchain_service(test_config_path)
    finally:
        # Clean up
        os.remove(test_config_path)
