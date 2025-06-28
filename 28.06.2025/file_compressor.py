# Filename:  file_compressor.py
import zipfile

def zip_files(directory, output_filename="archive.zip"):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file))

import os