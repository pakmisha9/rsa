import unittest
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from main import generate_rsa_keys, encrypt_message, decrypt_message

class TestGenerateRSAKeys(unittest.TestCase):

    def test_generate_rsa_keys(self):
        private_key, public_key = rsa_key_generator.generate_rsa_keys()

        # Check if private key is generated
        self.assertIsNotNone(private_key)
        self.assertTrue(private_key.has_private())

        # Check if public key is generated
        self.assertIsNotNone(public_key)
        self.assertFalse(public_key.has_private())

        # Check if public exponent is correct
        self.assertEqual(public_key.public_numbers().e, 65537)

        # Check if key size is correct
        self.assertEqual(private_key.key_size, 2048)
        self.assertEqual(public_key.key_size, 2048)

if __name__ == '__main__':
    unittest.main()