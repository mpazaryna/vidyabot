import os

import pytest
import yaml

from api.src.langchain.langchain_service import LangChainService


@pytest.fixture(scope="module")
def gemini_config():
    config = {
        "llm": {"default": "gemini", "options": ["openai", "gemini"]},
        "openai": {"api_key_env": "OPENAI_API_KEY"},
        "gemini": {"api_key_env": "GOOGLE_API_KEY"},
    }

    with open("test_gemini_config.yaml", "w") as file:
        yaml.dump(config, file)

    yield "test_gemini_config.yaml"

    os.remove("test_gemini_config.yaml")


def test_gemini_response(gemini_config, capsys):
    if not os.getenv("GOOGLE_API_KEY"):
        pytest.skip("GOOGLE_API_KEY not set in environment")

    service = LangChainService(gemini_config)

    # Test cases with different prompts and inputs
    test_cases = [
        {
            "prompt": "You are a helpful assistant. Provide a detailed response to the following: {input}",
            "input": "What is the capital of France and describe its significance.",
        },
        {
            "prompt": "You are a knowledgeable historian. Explain the following in depth: {input}",
            "input": "What were the main causes of World War I?",
        },
        {
            "prompt": "You are a creative storyteller. Create a short story based on the following prompt: {input}",
            "input": "A mysterious package arrives at the doorstep.",
        },
    ]

    for case in test_cases:
        try:
            response = service.generate_response(case["prompt"], case["input"])
            print(f"\n--- Gemini Response for: {case['input']} ---")
            print(f"Response type: {type(response)}")
            print(f"Response content:\n{response}")
            print("------------------------")
        except Exception as e:
            print(f"Error type: {type(e)}")
            print(f"Error message: {str(e)}")
            pytest.fail(f"Error generating response: {str(e)}")

    # Capture and print all output
    captured = capsys.readouterr()
    print(captured.out)


if __name__ == "__main__":
    pytest.main([__file__])
