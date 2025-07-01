# Filename:  file_reader.py
def read_file_contents(filepath):
    """Reads and returns the contents of a file."""
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."