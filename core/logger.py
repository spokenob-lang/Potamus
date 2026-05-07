import logging
from rich.logging import RichHandler
from config.settings import LOG_LEVEL

def setup_logger():
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format="%(message)s",
        handlers=[
            RichHandler(
                show_time=False,
                show_path=False,
                markup=False
            )
        ]
    )

def get_logger(name: str):
    return logging.getLogger(name)