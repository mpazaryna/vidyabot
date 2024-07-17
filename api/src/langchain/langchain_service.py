# flake8: noqa: W293
import logging
import os

import yaml
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LangChainService:
    def __init__(self, config_path="config.yaml"):
        self.config = self.load_config(config_path)
        self.llm = self.initialize_llm()
        self.memory = ConversationBufferMemory(return_messages=True)

    def load_config(self, config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)

    def initialize_llm(self):
        llm_type = self.config["llm"]["default"]
        if llm_type not in self.config["llm"]["options"]:
            raise ValueError(f"Unsupported LLM type: {llm_type}")

        api_key_env = self.config[llm_type]["api_key_env"]
        api_key = os.getenv(api_key_env)

        if not api_key:
            raise ValueError(
                f"API key not found in environment variable: {api_key_env}"
            )

        if llm_type == "openai":
            return OpenAI(api_key=api_key)
        elif llm_type == "gemini":
            return ChatGoogleGenerativeAI(
                google_api_key=api_key,
                model="gemini-pro",
                temperature=0.7,  # Adjust for more creative responses
                max_output_tokens=1024,  # Allow for longer responses
            )

    def generate_response(self, prompt, input_text):
        logger.debug(f"Generating response for input: {input_text}")
        prompt_template = PromptTemplate(
            input_variables=["history", "input"], template=prompt
        )

        chain = (
            {"history": RunnablePassthrough(), "input": RunnablePassthrough()}
            | prompt_template
            | self.llm
        )

        try:
            logger.debug("Invoking chain")
            response = chain.invoke(
                {"history": self.memory.buffer, "input": input_text}
            )
            logger.debug(f"Raw response: {response}")

            if isinstance(response, str):
                content = response
            elif hasattr(response, "content"):
                content = response.content
            else:
                content = str(response)

            logger.debug(f"Processed content: {content}")

            self.memory.chat_memory.add_user_message(input_text)
            self.memory.chat_memory.add_ai_message(content)

            return content
        except Exception as e:
            logger.exception("Error in generate_response")
            raise

    def summarize_text(self, text):
        summary_prompt = PromptTemplate(
            input_variables=["text"],
            template="Please provide a concise summary of the following text:\n\n{text}\n\nSummary:",
        )

        chain = summary_prompt | self.llm

        try:
            return chain.invoke({"text": text})
        except Exception as e:
            logging.exception("Error in summarize_text")
            raise

    def answer_question(self, question, context):
        qa_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="Context: {context}\n\nQuestion: {question}\n\nAnswer:",
        )

        chain = qa_prompt | self.llm

        try:
            return chain.invoke({"context": context, "question": question})
        except Exception as e:
            logging.exception("Error in answer_question")
            raise

    def translate_text(self, text, target_language):
        translation_prompt = PromptTemplate(
            input_variables=["target_language", "text"],
            template="Translate the following text to {target_language}:\n\n{text}\n\nTranslation:",
        )

        chain = translation_prompt | self.llm

        try:
            return chain.invoke({"target_language": target_language, "text": text})
        except Exception as e:
            logging.exception("Error in translate_text")
            raise


def get_langchain_service(config_path="config.yaml"):
    return LangChainService(config_path)
