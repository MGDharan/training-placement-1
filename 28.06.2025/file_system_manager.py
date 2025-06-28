# Filename: file_system_manager.py
import os
import shutil

class FileSystemManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_directory(self, dir_name):
        path = os.path.join(self.base_dir, dir_name)
        os.makedirs(path, exist_ok=True)

    def copy_file(self, source, destination):
        source_path = os.path.join(self.base_dir, source)
        destination_path = os.path.join(self.base_dir, destination)
        shutil.copy2(source_path, destination_path) # copy2 preserves metadata

    def delete_file(self, file_name):
        path = os.path.join(self.base_dir, file_name)
        if os.path.exists(path):
            os.remove(path)