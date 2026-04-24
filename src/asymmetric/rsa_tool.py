

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


class RSAModule:
    """Handle RSA asymmetric encryption"""
    
    @staticmethod
    def generate_key_pair(key_size=2048):
        """
        Generate RSA key pair
        Args:
            key_size: Key size in bits (default: 2048, recommended: 2048 or 4096)
        Returns:
            tuple: (private_key_pem, public_key_pem)
        """
        if key_size not in [1024, 2048, 3072, 4096]:
            raise ValueError("Key size must be 1024, 2048, 3072, or 4096 bits")
        
        key = RSA.generate(key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        return private_key.decode('utf-8'), public_key.decode('utf-8')
    
    @staticmethod
    def display_keys(private_key_pem, public_key_pem):
        """
        Display keys in formatted output
        Args:
            private_key_pem: Private key in PEM format
            public_key_pem: Public key in PEM format
        """
        print("=" * 60)
        print("RSA KEY PAIR GENERATED")
        print("=" * 60)
        print("\n🔒 PRIVATE KEY (Keep this SECRET!):")
        print(private_key_pem)
        print("\n🔓 PUBLIC KEY (Can be shared):")
        print(public_key_pem)
        print("=" * 60)
    
    @staticmethod
    def encrypt(plaintext, key_pem):
        """
        Encrypt plaintext using RSA
        Args:
            plaintext: String to encrypt
            key_pem: Public or Private key in PEM format
        Returns:
            str: Hex-encoded ciphertext
        """
        try:
            key = RSA.import_key(key_pem)
            cipher = PKCS1_OAEP.new(key)
            plaintext_bytes = plaintext.encode('utf-8')
            
            # Check plaintext size (RSA has message length limit)
            max_length = (key.size_in_bits() // 8) - 42  # OAEP overhead
            if len(plaintext_bytes) > max_length:
                raise ValueError(
                    f"Plaintext too long. Max {max_length} bytes for {key.size_in_bits()}-bit key. "
                    f"Got {len(plaintext_bytes)} bytes."
                )
            
            ciphertext = cipher.encrypt(plaintext_bytes)
            return binascii.hexlify(ciphertext).decode('utf-8')
        
        except ValueError as e:
            if "RSA key format is not supported" in str(e):
                raise ValueError("Invalid key format. Please provide a valid PEM key.")
            raise ValueError(f"Encryption failed: {e}")
    
    @staticmethod
    def decrypt(ciphertext_hex, key_pem):
        """
        Decrypt ciphertext using RSA
        Args:
            ciphertext_hex: Hex-encoded ciphertext
            key_pem: Private or Public key in PEM format
        Returns:
            str: Decrypted plaintext
        """
        try:
            key = RSA.import_key(key_pem)
            cipher = PKCS1_OAEP.new(key)
            ciphertext = binascii.unhexlify(ciphertext_hex)
            plaintext_bytes = cipher.decrypt(ciphertext)
            return plaintext_bytes.decode('utf-8')
        
        except ValueError as e:
            if "Ciphertext with incorrect length" in str(e):
                raise ValueError("Invalid ciphertext or wrong key used for decryption")
            if "RSA key format is not supported" in str(e):
                raise ValueError("Invalid key format. Please provide a valid PEM key.")
            raise ValueError(f"Decryption failed: {e}")
        except binascii.Error:
            raise ValueError("Ciphertext must be a valid hexadecimal string")
    
    @staticmethod
    def get_key_info(key_pem):
        """
        Get information about RSA key
        Args:
            key_pem: Key in PEM format
        Returns:
            dict: Key information (type, size, etc.)
        """
        try:
            key = RSA.import_key(key_pem)
            return {
                "has_private": key.has_private(),
                "key_size": key.size_in_bits(),
                "can_encrypt": True,
                "can_decrypt": key.has_private(),
                "max_message_length": (key.size_in_bits() // 8) - 42
            }
        except ValueError:
            raise ValueError("Invalid key format")


# ============== DEMO/TEST FUNCTIONS ==============

def demo_rsa_basic():
    """Basic RSA encryption/decryption demo"""
    print("\n" + "=" * 60)
    print("RSA BASIC DEMO - Encrypt with Public, Decrypt with Private")
    print("=" * 60)
    
    # Generate key pair
    private_key, public_key = RSAModule.generate_key_pair(2048)
    RSAModule.display_keys(private_key, public_key)
    
    # Encrypt with public key
    plaintext = "Hello RSA! This is a secret message."
    print(f"\nPlaintext: {plaintext}")
    ciphertext = RSAModule.encrypt(plaintext, public_key)
    print(f"Ciphertext (hex): {ciphertext[:80]}...")
    
    # Decrypt with private key
    decrypted = RSAModule.decrypt(ciphertext, private_key)
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")


def demo_rsa_reverse():
    """RSA reverse demo - showing encryption works both ways"""
    print("\n" + "=" * 60)
    print("RSA REVERSE DEMO - Encrypt with Private Key")
    print("=" * 60)
    print("Note: RSA encryption with private key is possible,")
    print("but decryption still requires the private key (not public).")
    
    # Generate key pair
    private_key, public_key = RSAModule.generate_key_pair(2048)
    
    # Encrypt with private key
    plaintext = "Signed message"
    print(f"\nPlaintext: {plaintext}")
    ciphertext = RSAModule.encrypt(plaintext, private_key)
    print(f"Ciphertext (hex): {ciphertext[:80]}...")
    
    # Decrypt with private key (correct way)
    decrypted = RSAModule.decrypt(ciphertext, private_key)
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")


def demo_key_info():
    """Display key information"""
    print("\n" + "=" * 60)
    print("KEY INFORMATION DEMO")
    print("=" * 60)
    
    private_key, public_key = RSAModule.generate_key_pair(2048)
    
    print("\nPrivate Key Info:")
    private_info = RSAModule.get_key_info(private_key)
    for key, value in private_info.items():
        print(f"  {key}: {value}")
    
    print("\nPublic Key Info:")
    public_info = RSAModule.get_key_info(public_key)
    for key, value in public_info.items():
        print(f"  {key}: {value}")


def demo_error_handling():
    """Test error handling"""
    print("\n" + "=" * 60)
    print("ERROR HANDLING DEMO")
    print("=" * 60)
    
    private_key, public_key = RSAModule.generate_key_pair(2048)
    plaintext = "Test"
    ciphertext = RSAModule.encrypt(plaintext, public_key)
    
    # Test 1: Wrong key for decryption
    print("\n1. Testing decryption with wrong key:")
    wrong_private, _ = RSAModule.generate_key_pair(2048)
    try:
        RSAModule.decrypt(ciphertext, wrong_private)
    except ValueError as e:
        print(f"   ✓ Caught error: {e}")
    
    # Test 2: Message too long
    print("\n2. Testing message too long:")
    long_message = "A" * 300  # Too long for 2048-bit key
    try:
        RSAModule.encrypt(long_message, public_key)
    except ValueError as e:
        print(f"   ✓ Caught error: {e}")
    
    # Test 3: Invalid ciphertext format
    print("\n3. Testing invalid ciphertext:")
    try:
        RSAModule.decrypt("INVALID_HEX", private_key)
    except ValueError as e:
        print(f"   ✓ Caught error: {e}")


def run_all_demos():
    # Run all demos
    demo_rsa_basic()
    demo_rsa_reverse()
    demo_key_info()
    demo_error_handling()
    
    print("\n" + "=" * 60)
    print("ALL DEMOS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
