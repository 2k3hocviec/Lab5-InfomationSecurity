import hashlib

def md5_hash(text):
    if not text.strip():
        raise ValueError("input cannot be empty")
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def sha256_hash(text):
    if not text.strip():
        raise ValueError("input cannot be empty")
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


    
