# Filename:  file_reader.py
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return "File not found."

filepath = "my_file.txt"  # Replace with your file path
file_contents = read_file(filepath)
print(file_contents)