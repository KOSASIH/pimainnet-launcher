import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file: str, log_level: str = 'INFO') -> None:
    """Set up logging with a rotating file handler"""
    log_level = getattr(logging, log_level.upper())
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
    handler.setLevel(log_level)
    logging.getLogger().addHandler(handler)
