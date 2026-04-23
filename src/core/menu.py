"""
Menu system for the cryptography toolkit
"""

from core.input_handler import InputHandler
from core.output_formatter import OutputFormatter
from symmetric.aes import AES

class Menu:
    """Main menu handler"""
    
    def __init__(self):
        """Initialize the menu"""
        self.input_handler = InputHandler()
        self.output_formatter = OutputFormatter()
    
    def display(self): 
        """Display the main menu"""
        while True:
            self.output_formatter.display_header("🔐 Cryptography Toolkit")
            print("Các tùy chọn chính:")
            print("1. AES ")
            print("2. DES")
            print("3. TRIPLEDES")
            print("4. HASH")
            print("0. Thoát (Exit)")
            
            choice = self.input_handler.get_valid_choice(["0", "1", "2", "3", "4"], "\nVui lòng chọn (0-3): ")
            
            if choice == "0":
                self.output_formatter.display_success("Cảm ơn đã sử dụng Cryptography Toolkit!")
                break
            elif choice == "1":
                self.displayAES()
            elif choice == "2":
                print("đang phát triển")
            elif choice == "3":
                print("đang phát triển")
            elif choice == "4":
                print("đang phát triển")
                
    def displayAES(self):
        """Display the main menu"""
        while True:
            self.output_formatter.display_header("🔐 Cryptography Toolkit")
            print("Các tùy chọn chính:")
            print("1. Mã hóa AES (Encryption)")
            print("2. Giải mã AES (Decryption)")
            print("3. Tạo khóa ngẫu nhiên (Generate Key)")
            print("0. Thoát (Exit)")
            
            choice = self.input_handler.get_valid_choice(["0", "1", "2", "3"], "\nVui lòng chọn (0-3): ")
            
            if choice == "0":
                self.output_formatter.display_success("Cảm ơn đã sử dụng Cryptography Toolkit!")
                break
            elif choice == "1":
                self.aes_encrypt()
            elif choice == "2":
                self.aes_decrypt()
            elif choice == "3":
                self.generate_aes_key()
    
    def aes_encrypt(self):
        """AES encryption menu"""
        self.output_formatter.display_header("🔐 Mã hóa AES (Encryption)")
        
        try:
            # Get key from user
            key = self.input_handler.get_user_input("Nhập khóa (16, 24 hoặc 32 ký tự): ").strip()
            
            # Get plaintext from user
            plaintext = self.input_handler.get_user_input("Nhập văn bản cần mã hóa: ").strip()
            
            if not key or not plaintext:
                self.output_formatter.display_error("Khóa và văn bản không được để trống!")
                return
            
            # Encrypt
            aes = AES(key)
            ciphertext = aes.encrypt(plaintext)
            
            if ciphertext.startswith("Error:"):
                self.output_formatter.display_error(ciphertext)
            else:
                self.output_formatter.display_result(ciphertext, "📝 Văn bản đã mã hóa:")
        
        except Exception as e:
            self.output_formatter.display_error(str(e))
    
    def aes_decrypt(self):
        """AES decryption menu"""
        self.output_formatter.display_header("🔓 Giải mã AES (Decryption)")
        
        try:
            # Get key from user
            key = self.input_handler.get_user_input("Nhập khóa (16, 24 hoặc 32 ký tự): ").strip()
            
            # Get ciphertext from user
            ciphertext = self.input_handler.get_user_input("Nhập văn bản đã mã hóa (Base64): ").strip()
            
            if not key or not ciphertext:
                self.output_formatter.display_error("Khóa và văn bản mã hóa không được để trống!")
                return
            
            # Decrypt
            aes = AES(key)
            plaintext = aes.decrypt(ciphertext)
            
            self.output_formatter.display_result(plaintext, "📄 Văn bản giải mã:")
        
        except Exception as e:
            self.output_formatter.display_error(str(e))
    
    def generate_aes_key(self):
        """Generate random AES key"""
        self.output_formatter.display_header("🔑 Tạo Khóa Ngẫu Nhiên")
        
        print("Chọn độ dài khóa:")
        print("1. 16 ký tự (128-bit)")
        print("2. 24 ký tự (192-bit)")
        print("3. 32 ký tự (256-bit)")
        
        choice = self.input_handler.get_valid_choice(["1", "2", "3"], "\nChọn (1-3): ")
        
        size_map = {"1": 16, "2": 24, "3": 32}
        size = size_map[choice]
        
        random_key = AES.generate_random_key(size)
        self.output_formatter.display_result(random_key, "🔑 Khóa ngẫu nhiên được tạo:")
