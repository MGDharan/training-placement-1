# Filename:  data_serializer.py
import pickle
def serialize_data(data, filepath):
    """Serializes data to a file using pickle."""
    try:
        with open(filepath, 'wb') as file:
            pickle.dump(data, file)
        return True
    except Exception as e:
        return f"Error: {e}"