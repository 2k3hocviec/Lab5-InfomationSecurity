"""
Input handler for user interactions
"""

class InputHandler:
    """Handles user input validation and processing"""
    
    @staticmethod
    def get_user_input(prompt):
        """Get and validate user input"""
        return input(prompt)
    
    @staticmethod
    def get_valid_choice(options, prompt="Chọn một tùy chọn: "):
        """Get valid choice from user"""
        while True:
            choice = input(prompt).strip()
            if choice in options:
                return choice
            print(f"Lỗi: Vui lòng chọn một trong các tùy chọn hợp lệ: {', '.join(options)}")
    
    @staticmethod
    def get_multiline_input(prompt):
        """Get multiline input from user"""
        print(prompt)
        print("(Nhấn Enter hai lần để kết thúc)")
        lines = []
        empty_count = 0
        while empty_count < 1:
            line = input()
            if line == "":
                empty_count += 1
            else:
                lines.append(line)
                empty_count = 0
        return "\n".join(lines)
    
    def get_multiline_input_rsa(self, prompt):
        """Get multiline input from the user"""
        print(prompt + " (Nhấn Ctrl+Z và Enter trên Windows hoặc Ctrl+D trên Linux/macOS để kết thúc)")
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        return "\n".join(lines)
