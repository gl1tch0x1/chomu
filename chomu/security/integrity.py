import hashlib
import os

def hash_file(filepath):
    if not os.path.exists(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(filepath, known_hash):
    current_hash = hash_file(filepath)
    return current_hash == known_hash, current_hash
