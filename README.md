
# Steganography

## Project Title: Steganography - Hiding Text Under Image

---

### Overview

This project is a part of the IBM Edunet Foundation Cybersecurity internship, which lasted for six Weeks. Throughout this internship, I gained practical knowledge about various cybersecurity tools and techniques, including VeraCrypt and setting up Kali Linux. The main focus of this project is to develop a steganography system to securely hide text messages within digital images.

---

### Repository Name: Steganography

---

### Files in the Repository:

- `encrypt.py`: Script for encoding secret messages into images.
- `decrypt.py`: Script for decoding hidden messages from images.
- `Steganography.pptx`: PowerPoint presentation detailing the project.
- `encryptedImage.jpg`: Sample encrypted image with a hidden message.
- `decryptedImage.jpg': Sample decrypted image.
---

### Project Description

**Steganography - Hiding Text Under Image:**

This project involves creating a steganographic system to embed confidential text messages into digital images using advanced encryption techniques. The project ensures that the hidden data remains imperceptible to unauthorized users while maintaining the image quality.

---

### Project Components

1. **Encryption Script (`encrypt.py`):**
   - Reads an input image.
   - Prompts the user for a secret message and password.
   - Uses SHA-256 hashing for password security.
   - Embeds the secret message into the image pixels.
   - Saves the encrypted image.

2. **Decryption Script (`decrypt.py`):**
   - Reads the encrypted image.
   - Prompts the user for the password.
   - Uses SHA-256 hashing to validate the password.
   - Extracts and decodes the hidden message from the image.
   - Displays the decoded message.

---

### How to Use

1. **Encryption:**
   - Ensure `encrypt.py` is in the same directory as your input image.
   - Run the script and follow the prompts to input your secret message and password.
   - The script will generate an `encryptedImage.jpg` file with the hidden message.

2. **Decryption:**
   - Ensure `decrypt.py` is in the same directory as your encrypted image.
   - Run the script and follow the prompts to input your password.
   - The script will display the hidden message.

---

### Tools and Libraries

- Python
- OpenCV
- hashlib

---

### Cloning the Repository

To copy or clone this repository to your local machine, use the following commands:

```bash
# Clone the repository
git clone https://github.com/abhinavsingh45/Steganography.git

# Change directory to the cloned repository
cd Steganography
