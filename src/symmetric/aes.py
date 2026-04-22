"""
AES encryption/decryption implementation
"""
import os
import base64
from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad, unpad

class AES:
    """AES encryption algorithm"""
    
    def __init__(self, key):
        """Initialize AES with a key"""
        self.key = key
        self.block_size = 16 # AES block size is 128 bits

    def validate_key(self):
        """Kiểm tra độ dài khóa (16, 24, 32 bytes) """
        key_bytes = self.key.encode('utf-8')
        if len(key_bytes) not in [16, 24, 32]:
            raise ValueError("Kích thước khóa không hợp lệ (Phải là 16, 24 hoặc 32 ký tự).")
        return key_bytes

    @staticmethod
    def generate_random_key(size=16):
        """Tạo khóa ngẫu nhiên cho người dùng (Auto-generate key)"""
        # Trả về dạng Hex để dễ hiển thị trên giao diện
        return os.urandom(size).hex()[:size]
    
    def encrypt(self, plaintext):
        """Mã hóa Plaintext sang Ciphertext (CBC mode)"""
        try:
            key = self.validate_key()
            # Khởi tạo Cipher với Mode CBC 
            cipher = CryptoAES.new(key, CryptoAES.MODE_CBC)
            
            # Padding dữ liệu theo chuẩn PKCS7 để khớp block size
            padded_data = pad(plaintext.encode('utf-8'), self.block_size)
            ct_bytes = cipher.encrypt(padded_data)
            
            # Gộp IV và Ciphertext sau đó mã hóa Base64 để hiển thị
            iv_and_ct = cipher.iv + ct_bytes
            return base64.b64encode(iv_and_ct).decode('utf-8')
        except Exception as e:
            return f"Error: {str(e)}"
    
    def decrypt(self, ciphertext):
        """Giải mã Ciphertext về Plaintext ban đầu [cite: 19, 26]"""
        try:
            key = self.validate_key()
            # Decode từ Base64
            iv_and_ct = base64.b64decode(ciphertext)
            
            # Tách IV (16 bytes đầu) và Ciphertext
            iv = iv_and_ct[:16]
            ct = iv_and_ct[16:]
            
            cipher = CryptoAES.new(key, CryptoAES.MODE_CBC, iv)
            # Giải mã và bóc padding (Unpad)
            pt_bytes = unpad(cipher.decrypt(ct), self.block_size)
            return pt_bytes.decode('utf-8')
        except Exception:
            return "Giải mã thất bại: Khóa sai hoặc dữ liệu hỏng."
