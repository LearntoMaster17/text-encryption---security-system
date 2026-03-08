# Text Encryption & Security System

This project provides a simple text coding and decoding tool for basic message encryption.

## Features
- **Coding:**
  - For words with 3+ characters: moves the first letter to the end, adds 3 random characters at the start and end.
  - For words with 2 or fewer characters: reverses the word.
- **Decoding:**
  - For words with 2 or fewer characters: reverses the word.
  - For words with 3+ characters: removes 3 characters from start and end, moves last letter to the beginning.

## Usage
Run the script:
```
python main.py
```
- Enter your message.
- Choose 0 to code or 1 to decode.

## Requirements
No external packages required (uses only Python standard library).
