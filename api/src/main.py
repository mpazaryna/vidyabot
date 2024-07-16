import logging
import os
from functools import lru_cache

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from .data.user_data import get_user_data
from .langchain.langchain_service import LangChainService

# Configure logging
logging.basicConfig(
    filename="server.log",
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Capture warnings and redirect them to the log
logging.captureWarnings(True)

app = FastAPI()


class Query(BaseModel):
    text: str


@lru_cache()
def get_langchain_service():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OpenAI API key not found")
        raise HTTPException(status_code=500, detail="OpenAI API key not found")
    return LangChainService(api_key)


@app.get("/users")
async def read_users():
    """
    Retrieve all users.

    Returns:
        list: A list of user dictionaries.

    Raises:
        HTTPException: If there's an error retrieving the user data.
    """
    try:
        users = get_user_data()
        return users
    except Exception as e:
        logging.exception("Error retrieving user data")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    """
    Root endpoint.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to the User API"}


@app.post("/generate_response")
async def generate_response(
    query: Query, service: LangChainService = Depends(get_langchain_service)
):
    prompt = "You are a helpful assistant. Respond to the following: {input}"
    try:
        response = service.generate_response(prompt, query.text)
        logging.info(f"Generated response for query: {query.text[:50]}...")
        return {"response": response}
    except Exception as e:
        logging.exception(f"Error generating response for query: {query.text[:50]}...")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
