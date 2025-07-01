# Filename:  data_deserializer.py
import pickle
def deserialize_data(filepath):
    """Deserializes data from a file using pickle."""
    try:
        with open(filepath, 'rb') as file:
            data = pickle.load(file)
            return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return None