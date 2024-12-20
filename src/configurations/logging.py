import logging
from os import getenv

from configurations.log_formatter import CustomFormatter

def config_logging():
    supress_logs()

    root = logging.getLogger()
    handler = logging.StreamHandler()

    environment = getenv("ENVIRONMENT", "DEV")

    log_level = logging.DEBUG if environment.upper() == "DEV" else logging.INFO

    handler.setLevel(log_level)
    root.setLevel(log_level) 
    
    handler.setFormatter(CustomFormatter())
    root.addHandler(handler)

def supress_logs():
    logging.getLogger("pika").setLevel(logging.WARNING)
