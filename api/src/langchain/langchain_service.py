# flake8: noqa: W293
import logging

from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI


class LangChainService:
    def __init__(self, api_key):
        self.llm = OpenAI(api_key=api_key)
        self.memory = ConversationBufferMemory(return_messages=True)

    def generate_response(self, prompt, input_text):
        prompt_template = PromptTemplate(
            input_variables=["history", "input"], template=prompt
        )

        chain = (
            {"history": RunnablePassthrough(), "input": RunnablePassthrough()}
            | prompt_template
            | self.llm
        )

        try:
            response = chain.invoke(
                {"history": self.memory.buffer, "input": input_text}
            )
            self.memory.save_context({"input": input_text}, {"output": response})
            return response
        except Exception as e:
            logging.exception("Error in generate_response")
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
