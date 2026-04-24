"""
Cryptography Toolkit - Main Entry Point
"""

from core.menu import Menu
from hash_utils import md5_hash, sha256_hash


def main():
    """Main entry point for the cryptography toolkit"""
    menu = Menu()
    menu.display()

if __name__ == "__main__":
    main()



