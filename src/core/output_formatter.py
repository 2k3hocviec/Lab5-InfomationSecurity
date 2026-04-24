"""
Output formatter for displaying results
"""

class OutputFormatter:
    """Formats and displays output to users"""
    
    @staticmethod
    def display_result(result, title="Kết quả:"):
        """Display formatted result"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60)
        print(result)
        print("="*60 + "\n")
    
    @staticmethod
    def display_error(error_msg):
        """Display error message"""
        print(f"\n❌ LỖI: {error_msg}\n")
    
    @staticmethod
    def display_success(msg):
        """Display success message"""
        print(f"\n✓ {msg}\n")
    
    @staticmethod
    def display_header(title):
        """Display header"""
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
