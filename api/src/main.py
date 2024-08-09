import logging

# from api.src.langchain.langchain_service import get_langchain_service
from aiforge.langchain.langchain_service import get_langchain_service
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from .data.user_data import get_user_data

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


class Query(BaseModel):
    text: str


async def get_langchain_service_dependency():
    try:
        logger.debug("Attempting to initialize LangChainService")
        service = await get_langchain_service()
        logger.debug(
            f"LangChainService initialized successfully. Using LLM: {service.config['llm']['default']}"
        )
        return service
    except Exception as e:
        logger.exception("Error initializing LangChainService")
        logger.error(f"Error details: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error initializing LLM service: {str(e)}"
        )


@app.post("/generate_response")
async def generate_response(
    query: Query, service=Depends(get_langchain_service_dependency)
):
    prompt = "You are a helpful assistant. Respond to the following: {input}"
    logger.debug(f"Received query: {query.text[:50]}...")
    logger.debug(f"Using LLM: {service.config['llm']['default']}")

    try:
        logger.debug("Calling service.generate_response")
        response = await service.generate_response(prompt, query.text)
        logger.info(f"Generated response for query: {query.text[:50]}...")
        logger.debug(f"Full response: {response}")
        return {"response": response}
    except Exception as e:
        logger.exception(f"Error generating response for query: {query.text[:50]}...")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
