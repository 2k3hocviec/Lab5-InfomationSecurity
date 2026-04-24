import hashlib

def md5_hash(text):
    if not text.strip():
        raise ValueError("input cannot be empty!")
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def sha256_hash(text):
    if not text.strip():
        raise ValueError("input cannot be empty!")
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def hash (): 
    print("Choose hash algorithm:")
    print("1. MD5")
    print("2. SHA-256")

    choice = input("Enter choice: ").strip()
    text = input("Enter text: ").strip()

    try:
        match choice:
            case "1":
                print("\n--- RESULT ---")
                print("MD5:", md5_hash(text))

            case "2":
                print("\n--- RESULT ---")
                print("SHA-256:", sha256_hash(text))

            case _:
                print("Invalid choice!")

    except Exception as e:
        print("Error:", e)