import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

# Default input and output paths
IMAGE_PATH = r"C:\Users\Snehitha\OneDrive\Desktop\encryptedImage.png"
OUTPUT_PATH = r"C:\Users\Snehitha\OneDrive\Desktop\encryptedImage123.png"
 
class EncryptGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Encryption")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter secret message:")
        layout.addWidget(self.label)

        self.message_input = QLineEdit(self)
        layout.addWidget(self.message_input)

        self.label2 = QLabel("Enter passcode:")
        layout.addWidget(self.label2)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.encrypt_button = QPushButton("Encrypt Image", self)
        self.encrypt_button.clicked.connect(self.encrypt_image)
        layout.addWidget(self.encrypt_button)

        self.setLayout(layout)

    def encrypt_image(self):
        message = self.message_input.text()
        password = self.password_input.text()

        if not message or not password:
            QMessageBox.warning(self, "Error", "Message and password cannot be empty!")
            return

        img = cv2.imread(IMAGE_PATH)
        if img is None:
            QMessageBox.warning(self, "Error", "Image not found or cannot be read.")
            return

        height, width, _ = img.shape
        max_bytes = height * width * 3 // 8  # Max bytes that can be stored

        # Encrypt message using XOR with password
        encrypted_message = self.xor_encrypt(message, password)
        encoded_message = f"{len(encrypted_message):04d}{encrypted_message}"  # Store length

        if len(encoded_message) > max_bytes:
            QMessageBox.warning(self, "Error", "Message too long for the selected image!")
            return

        # Embed encrypted message in the image
        img_flat = img.flatten()
        for i, char in enumerate(encoded_message):
            img_flat[i] = ord(char)

        encrypted_img = img_flat.reshape(img.shape)
        cv2.imwrite(OUTPUT_PATH, encrypted_img)

        QMessageBox.information(self, "Success", f"Message encrypted successfully!\nSaved at: {OUTPUT_PATH}")

    @staticmethod
    def xor_encrypt(text, key):
        return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptGUI()
    window.show()
    sys.exit(app.exec())
