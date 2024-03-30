from cryptography.hazmat.primitives import padding

class TestEncryptMessage(unittest.TestCase):

    def test_encrypt_message(self):
        # Generate RSA keys
        private_key, public_key = rsa_key_generator.generate_rsa_keys()

        # Test encryption with a message
        message = "Hello, world!"
        encrypted_message = encrypt_message(message, public_key)

        # Check if the message is encrypted
        self.assertNotEqual(encrypted_message, message.encode())

        # Decrypt the message using the private key for verification
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

        # Check if the decrypted message matches the original message
        self.assertEqual(decrypted_message, message)

if __name__ == '__main__':
    unittest.main()