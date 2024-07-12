# File: scripts/run_server.py

import logging
import os
import sys
from datetime import datetime

import uvicorn


def setup_logging():
    log_file = "server.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    sys.stdout = open(log_file, "a")
    sys.stderr = sys.stdout
    print(f"\n--- Server started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")


def run_server():
    setup_logging()
    try:
        uvicorn.run(
            "api.src.main:app",
            host="0.0.0.0",
            port=8000,
            log_level="info",
            access_log=True,
        )
    except Exception as e:
        logging.error(f"An error occurred while running the server: {str(e)}")
        print(f"An error occurred while running the server: {str(e)}")


if __name__ == "__main__":
    run_server()
