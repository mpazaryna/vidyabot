# File: scripts/start_server.py

import argparse

import uvicorn


def main():
    """Start the FastAPI server."""
    parser = argparse.ArgumentParser(description="Start the FastAPI server.")
    parser.add_argument(
        "--env",
        choices=["dev", "prod"],
        default="dev",
        help="Specify the environment (dev or prod)",
    )
    args = parser.parse_args()

    uvicorn.run(
        "api.src.main:app", host="0.0.0.0", port=8000, reload=(args.env == "dev")
    )


if __name__ == "__main__":
    main()
