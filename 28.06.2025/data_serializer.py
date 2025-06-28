# Filename:  data_serializer.py
import json

def serialize_data(data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def deserialize_data(filename="data.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None