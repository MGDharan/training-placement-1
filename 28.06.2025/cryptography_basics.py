# Filename:  cryptography_basics.py
import hashlib

def hash_string(text, algorithm='sha256'):
    if algorithm == 'sha256':
        hasher = hashlib.sha256()
    elif algorithm == 'md5':
        hasher = hashlib.md5()
    else:
        raise ValueError("Unsupported hashing algorithm.")
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()