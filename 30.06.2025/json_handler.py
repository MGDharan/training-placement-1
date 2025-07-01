# Filename:  json_handler.py
import json
def read_json_file(filepath):
    """Reads and parses a JSON file."""
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return None