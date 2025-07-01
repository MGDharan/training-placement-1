# Filename:  logging_example.py
import logging
logging.basicConfig(filename='my_log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    """Logs an error message."""
    logging.error(message)