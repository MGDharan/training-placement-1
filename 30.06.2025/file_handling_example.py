# Filename:  file_handling_example.py
def write_to_file(filepath, content):
    """Writes content to a file, creating the file if it doesn't exist."""
    try:
        with open(filepath, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        return f"An error occurred: {e}"