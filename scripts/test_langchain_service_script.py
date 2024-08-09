import logging
import os

from api.src.langchain.langchain_service import get_langchain_service

# from aiforge.langchain.langchain_service import get_langchain_service

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    try:
        logger.debug("Initializing LangChainService")
        service = get_langchain_service()

        prompt = "You are a helpful assistant. Respond to the following: {input}"
        input_text = "What is the capital of France?"

        logger.debug(f"Generating response for input: {input_text}")
        response = service.generate_response(prompt, input_text)

        logger.info(f"Generated response: {response}")
    except Exception:
        logger.exception("An error occurred:")


if __name__ == "__main__":
    logger.debug(f"GOOGLE_API_KEY set: {'GOOGLE_API_KEY' in os.environ}")
    logger.debug(f"OPENAI_API_KEY set: {'OPENAI_API_KEY' in os.environ}")
    main()
