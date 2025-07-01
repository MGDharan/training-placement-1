# Filename:  csv_reader.py
import csv
def read_csv_file(filepath):
    """Reads and returns data from a CSV file."""
    data = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return None