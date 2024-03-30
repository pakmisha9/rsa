import unittest
from cryptography.hazmat.primitives.asymmetric import rsa

from main import generate_rsa_keys, encrypt_message, decrypt_message

class TestRSAEncryption(unittest.TestCase):

    def test_encrypt_decrypt(self):
        # Генерируем ключи
        private_key, public_key = generate_rsa_keys()

        # Сообщение для шифрования
        message = "Hello, RSA!"

        # Шифруем сообщение
        encrypted_message = encrypt_message(message, public_key)

        # Дешифруем сообщение
        decrypted_message = decrypt_message(encrypted_message, private_key)

        # Проверяем, что исходное сообщение равно дешифрованному
        self.assertEqual(message, decrypted_message)

if __name__ == "__main__":
    unittest.main()