import unittest
from src.Logic.AesEncryption import AesEncryption
from src.Logic.EncryptionContext import EncryptionContext
from src.Logic.ErrorsAndExceptions import ErrorsAndExceptions

class EncryptionTest(unittest.TestCase):

    def setUp(self):
        self.encryption_strategy = AesEncryption()
        self.encryption_context = EncryptionContext(self.encryption_strategy)
        self.errors = ErrorsAndExceptions(self.encryption_context)

    def test_encrypt_correctly(self):
        message = "Hello World"
        key = "mysecretkey1234"
        encrypted_message = self.encryption_context.encrypt_message(message, key)
        self.assertNotEqual(message, encrypted_message)
        decrypted_message = self.encryption_context.decrypt_message(encrypted_message, key)
        self.assertEqual(message, decrypted_message)

    def test_encrypt_empty_message_error(self):
        result = self.errors.encrypt_empty_message()
        self.assertIn("Error", result)

    def test_encrypt_list_error(self):
        result = self.errors.encrypt_list()
        self.assertIn("Error", result)

    def test_encrypt_integer_error(self):
        result = self.errors.encrypt_integer()
        self.assertIn("Error", result)

    def test_decrypt_empty_message_error(self):
        result = self.errors.decrypt_empty_message()
        self.assertIn("Error", result)

if __name__ == '__main__':
    unittest.main()
