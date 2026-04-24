# Cryptography Toolkit

A comprehensive Python toolkit for cryptographic operations including encryption, decryption, and hashing.

## Features

- **Symmetric Encryption**
  - AES (Advanced Encryption Standard)
  - DES (Data Encryption Standard)
  - Triple DES

- **Asymmetric Encryption**
  - RSA

- **Hashing**
  - MD5
  - SHA-1
  - SHA-256
  - SHA-512

- **Utilities**
  - Encoding/Decoding (Base64, Hex)
  - Key Generation
  - Input Validation

## Project Structure

```
cryptography-toolkit/
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── menu.py
│   │   ├── input_handler.py
│   │   └── output_formatter.py
│   ├── symmetric/
│   │   ├── aes.py
│   │   ├── des.py
│   │   └── tripledes.py
│   ├── asymmetric/
│   │   └── rsa_tool.py
│   ├── hash/
│   │   └── digest_tool.py
│   └── utils/
│       ├── encoding.py
│       ├── keygen.py
│       └── validators.py
├── docs/
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```

## Requirements

- Python 3.7+

## License

MIT License
