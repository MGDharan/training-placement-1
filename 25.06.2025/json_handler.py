# Filename:  json_handler.py
import json

def read_json(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def write_json(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        return False


data = {"name": "John Doe", "age": 30, "city": "New York"}
filepath = "data.json"

write_json(filepath,data)
read_data = read_json(filepath)
print(read_data)