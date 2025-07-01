# Filename: file_line_counter.py
def count_lines_in_file(filepath):
    """Counts the number of lines in a file."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0