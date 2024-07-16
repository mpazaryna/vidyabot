import logging

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "use_colors": None,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": "server.log",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "WARNING"},
    },
}

# Capture warnings
logging.captureWarnings(True)
