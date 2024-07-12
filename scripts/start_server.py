# File: scripts/start_server.py

import logging

import uvicorn

from api.src.main import app

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        filename="server.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Configure Uvicorn to use the root logger
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers = logging.getLogger().handlers

    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None,  # Disables Uvicorn's default logging configuration
    )
