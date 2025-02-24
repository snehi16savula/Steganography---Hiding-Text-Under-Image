import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

# Encrypted image path
IMAGE_PATH = r"C:\Users\Shiva Prasad\OneDrive\Desktop\encryptedImage123.png"

class DecryptGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Decryption")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter passcode for decryption:")
        layout.addWidget(self.label)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.decrypt_button = QPushButton("Decrypt Image", self)
        self.decrypt_button.clicked.connect(self.decrypt_image)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    def decrypt_image(self):
        password_attempt = self.password_input.text()
        if not password_attempt:
            QMessageBox.warning(self, "Error", "Please enter the password to decrypt!")
            return

        img = cv2.imread(IMAGE_PATH)
        if img is None:
            QMessageBox.warning(self, "Error", "Encrypted image not found.")
            return

        height, width, _ = img.shape
        img_flat = img.flatten()

        # Extract message length
        try:
            message_length = int("".join(chr(img_flat[i]) for i in range(4)))
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid encrypted data format.")
            return

        encrypted_message = "".join(chr(img_flat[i]) for i in range(4, 4 + message_length))

        # Decrypt message using XOR
        decrypted_message = self.xor_decrypt(encrypted_message, password_attempt)

        if decrypted_message is None:
            QMessageBox.warning(self, "Error", "Incorrect password! Access denied.")
        else:
            QMessageBox.information(self, "Decryption Successful", f"Secret Message: {decrypted_message}")

    @staticmethod
    def xor_decrypt(text, key):
        try:
            return "".join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))
        except:
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecryptGUI()
    window.show()
    sys.exit(app.exec())
