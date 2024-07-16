# flake8: noqa: W293
import os

import pytest

from api.src.langchain.langchain_service import LangChainService


@pytest.fixture(scope="module")
def langchain_service():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY environment variable not set")
    return LangChainService(api_key)


def test_generate_response(langchain_service):
    prompt = "You are a helpful assistant. Respond to the following: {input}"
    input_text = "Tell me about artificial intelligence."
    response = langchain_service.generate_response(prompt, input_text)
    assert response, "Response should not be empty"
    assert isinstance(response, str), "Response should be a string"
    assert len(response) > 10, "Response should be a meaningful length"


def test_summarize_text(langchain_service):
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    summary = langchain_service.summarize_text(text)
    assert summary, "Summary should not be empty"
    assert isinstance(summary, str), "Summary should be a string"
    assert len(summary) < len(text), "Summary should be shorter than original text"


def test_answer_question(langchain_service):
    context = "Paris is the capital and most populous city of France."
    question = "What is the capital of France?"
    answer = langchain_service.answer_question(question, context)
    assert answer, "Answer should not be empty"
    assert isinstance(answer, str), "Answer should be a string"
    assert "Paris" in answer, "Answer should contain 'Paris'"


def test_translate_text(langchain_service):
    text = "Hello, how are you?"
    target_language = "Spanish"
    translation = langchain_service.translate_text(text, target_language)
    assert translation, "Translation should not be empty"
    assert isinstance(translation, str), "Translation should be a string"
    assert translation != text, "Translation should be different from original text"
    assert "Hola" in translation, "Spanish translation should contain 'Hola'"
