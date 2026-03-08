# Text Encryption & Security System

A Python-based command-line application for secure text encoding and decoding. This project demonstrates custom encryption logic, user input handling, and string manipulation skills in Python.

---

## Project Overview

The **Text Encryption & Security System** allows users to encode and decode messages using a custom algorithm. It is designed for educational purposes and demonstrates the fundamentals of string transformation and basic cryptography.

---

## Key Features

- **Custom Encoding Algorithm**:  
  - For words with 3 or more characters: moves the first letter to the end, adds 3 random characters at the start and end.
  - For words with less than 3 characters: simply reverses the string.
- **Custom Decoding Algorithm**:  
  - For words with 3 or more characters: removes 3 characters from start and end, moves the last letter to the front.
  - For words with less than 3 characters: reverses the string.
- **Interactive CLI**:  
  - User chooses to encode or decode and enters the message interactively.
- **Randomization**:  
  - Uses random letters and digits for added obfuscation in encoding.
- **Educational Value**:  
  - Great for learning about string manipulation and basic encryption concepts.

---

## Technologies Used

- Python 3

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/text-encryption---security-system.git
   cd text-encryption---security-system
   ```
2. Install the required package (if not already installed):
   ```bash
   pip install -r requirement.txt
   ```

---

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Follow the prompts to choose encoding or decoding and enter your message.

---

## File Structure

- `main.py`  
  Main script for encoding and decoding messages.
- `requirement.txt`  
  List of required Python packages.

---

## Example

- **Encoding:**
  - Input: `hello world`
  - Output: (randomized, e.g.) `a1Belloh2K d9Worlw8Z`
- **Decoding:**
  - Input: (encoded string)
  - Output: `hello world`

---

## Skills Demonstrated

- String manipulation and transformation in Python
- Custom encryption/decryption logic
- Command-line application development
- User input validation and error handling

---

## Contact

For any queries or collaboration opportunities, please reach out via GitHub or LinkedIn.

---

**Showcase your Python logic and security fundamentals with this project!**
