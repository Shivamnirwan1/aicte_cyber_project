# Secure Data Hiding in Image Using Steganography

## Problem Statement
Traditional encryption methods make it obvious that data is being protected, which can attract unwanted attention. Steganography allows secure data hiding within images, making the existence of the message undetectable to an unauthorized party. This project implements an efficient and secure method of embedding and extracting secret messages in images using steganography.

## Technology Used
- **Programming Language**: Python
- **Libraries**: OpenCV, NumPy, hashlib, os
- **Concepts**: Image Processing, Steganography, Cryptography

## Features
- Secure data embedding in images without noticeable distortion.
- Password-protected encryption and decryption.
- Hash-based password verification for added security.
- Efficient and lightweight implementation using Python.

## End Users
- Cybersecurity professionals
- Digital forensics experts
- Privacy-conscious individuals
- Researchers in data security and cryptography

## Installation & Usage
### Prerequisites
Ensure you have Python installed along with the necessary dependencies:
```sh
pip install opencv-python numpy
```

### Running the Project
1. Place the image file in the project directory.
2. Run the encryption script to hide a secret message:
   ```sh
   python encrypt.py
   ```
3. Enter your secret message and a passcode.
4. The encrypted image will be saved.
5. Run the decryption script to reveal the hidden message:
   ```sh
   python decrypt.py
   ```
6. Enter the correct passcode to retrieve the message.

## Conclusion
This project demonstrates the power of steganography for secure communication. By embedding data into images, it provides an effective way to conceal sensitive information while maintaining confidentiality. This technique can be extended for secure data transmission, watermarking, and anti-tampering measures.

