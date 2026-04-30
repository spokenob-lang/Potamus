import logging
from rich.logging import RichHandler

def setup_logger(level="INFO"):
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[RichHandler(show_time=False, show_path=False)]
    )

def get_logger(name: str):
    return logging.getLogger(name)