

from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii


class DES:
    """Handle DES encryption and decryption"""
    
    @staticmethod
    def generate_key():
        """Generate a random 8-byte DES key"""
        return get_random_bytes(8)
    
    @staticmethod
    def validate_key(key_hex):
        """
        Validate DES key format and size
        Args:
            key_hex: Hexadecimal string of the key
        Returns:
            bytes: Valid key if successful
        Raises:
            ValueError: If key is invalid
        """
        try:
            key = binascii.unhexlify(key_hex)
            if len(key) != 8:
                raise ValueError(f"DES key must be 8 bytes (16 hex chars). Got {len(key)} bytes.")
            return key
        except binascii.Error:
            raise ValueError("Key must be a valid hexadecimal string")
    
    @staticmethod
    def encrypt(plaintext, key):
        """
        Encrypt plaintext using DES
        Args:
            plaintext: String to encrypt
            key: 8-byte key (bytes)
        Returns:
            str: Hex-encoded ciphertext
        """
        cipher = DES.new(key, DES.MODE_ECB)
        plaintext_bytes = plaintext.encode('utf-8')
        padded_data = pad(plaintext_bytes, DES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        return binascii.hexlify(ciphertext).decode('utf-8')
    
    @staticmethod
    def decrypt(ciphertext_hex, key):
        """
        Decrypt ciphertext using DES
        Args:
            ciphertext_hex: Hex-encoded ciphertext
            key: 8-byte key (bytes)
        Returns:
            str: Decrypted plaintext
        """
        try:
            cipher = DES.new(key, DES.MODE_ECB)
            ciphertext = binascii.unhexlify(ciphertext_hex)
            decrypted_padded = cipher.decrypt(ciphertext)
            plaintext_bytes = unpad(decrypted_padded, DES.block_size)
            return plaintext_bytes.decode('utf-8')
        except ValueError as e:
            raise ValueError(f"Decryption failed: {e}")
        except binascii.Error:
            raise ValueError("Ciphertext must be a valid hexadecimal string")


class DES3Module:
    """Handle 3DES (Triple DES) encryption and decryption"""
    
    @staticmethod
    def generate_key():
        """Generate a random 24-byte 3DES key"""
        return get_random_bytes(24)
    
    @staticmethod
    def validate_key(key_hex):
        """
        Validate 3DES key format and size
        Args:
            key_hex: Hexadecimal string of the key
        Returns:
            bytes: Valid key if successful
        Raises:
            ValueError: If key is invalid
        """
        try:
            key = binascii.unhexlify(key_hex)
            if len(key) not in [16, 24]:
                raise ValueError(
                    f"3DES key must be 16 bytes (32 hex) or 24 bytes (48 hex). "
                    f"Got {len(key)} bytes."
                )
            return key
        except binascii.Error:
            raise ValueError("Key must be a valid hexadecimal string")
    
    @staticmethod
    def encrypt(plaintext, key):
        """
        Encrypt plaintext using 3DES
        Args:
            plaintext: String to encrypt
            key: 16 or 24-byte key (bytes)
        Returns:
            str: Hex-encoded ciphertext
        """
        cipher = DES3.new(key, DES3.MODE_ECB)
        plaintext_bytes = plaintext.encode('utf-8')
        padded_data = pad(plaintext_bytes, DES3.block_size)
        ciphertext = cipher.encrypt(padded_data)
        return binascii.hexlify(ciphertext).decode('utf-8')
    
    @staticmethod
    def decrypt(ciphertext_hex, key):
        """
        Decrypt ciphertext using 3DES
        Args:
            ciphertext_hex: Hex-encoded ciphertext
            key: 16 or 24-byte key (bytes)
        Returns:
            str: Decrypted plaintext
        """
        try:
            cipher = DES3.new(key, DES3.MODE_ECB)
            ciphertext = binascii.unhexlify(ciphertext_hex)
            decrypted_padded = cipher.decrypt(ciphertext)
            plaintext_bytes = unpad(decrypted_padded, DES3.block_size)
            return plaintext_bytes.decode('utf-8')
        except ValueError as e:
            raise ValueError(f"Decryption failed: {e}")
        except binascii.Error:
            raise ValueError("Ciphertext must be a valid hexadecimal string")


# ============== DEMO/TEST FUNCTIONS ==============

def demo_des():
    """Demo DES encryption and decryption"""
    print("=" * 60)
    print("DES ENCRYPTION DEMO")
    print("=" * 60)
    
    # Generate random key
    key = DESModule.generate_key()
    key_hex = binascii.hexlify(key).decode('utf-8')
    print(f"Generated Key (hex): {key_hex}")
    
    # Encrypt
    plaintext = "Hello DES!"
    print(f"Plaintext: {plaintext}")
    ciphertext = DESModule.encrypt(plaintext, key)
    print(f"Ciphertext (hex): {ciphertext}")
    
    # Decrypt
    decrypted = DESModule.decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}\n")


def demo_3des():
    """Demo 3DES encryption and decryption"""
    print("=" * 60)
    print("3DES ENCRYPTION DEMO")
    print("=" * 60)
    
    # Generate random key
    key = DES3Module.generate_key()
    key_hex = binascii.hexlify(key).decode('utf-8')
    print(f"Generated Key (hex): {key_hex}")
    
    # Encrypt
    plaintext = "Hello Triple DES!"
    print(f"Plaintext: {plaintext}")
    ciphertext = DES3Module.encrypt(plaintext, key)
    print(f"Ciphertext (hex): {ciphertext}")
    
    # Decrypt
    decrypted = DES3Module.decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}\n")


if __name__ == "__main__":
    # Run demos
    demo_des()
    demo_3des()
    
    # Test with manual key
    print("=" * 60)
    print("MANUAL KEY TEST")
    print("=" * 60)
    manual_key_hex = "0123456789abcdef"  # 8 bytes = 16 hex chars
    try:
        key = DESModule.validate_key(manual_key_hex)
        plaintext = "Test message"
        ciphertext = DESModule.encrypt(plaintext, key)
        print(f"Manual Key: {manual_key_hex}")
        print(f"Plaintext: {plaintext}")
        print(f"Ciphertext: {ciphertext}")
        print(f"Decrypted: {DESModule.decrypt(ciphertext, key)}")
    except ValueError as e:
        print(f"Error: {e}")
