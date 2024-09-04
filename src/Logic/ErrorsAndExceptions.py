class ErrorsAndExceptions:
    """Class to simulate encryption and decryption errors."""
    
    def __init__(self, encryption_context):
        self.encryption_context = encryption_context

    def encrypt_without_key(self):
        message = "Hello, how are you?"
        key = ""

        try:
            if not key:
                raise KeyError("Cannot encrypt without a key.")
            self.encryption_context.encrypt_message(message, key)
        except KeyError as e:
            return f"Error: {e}"

    def encrypt_empty_message(self):
        message = "" or None
        key = "123"

        try:
            if not message:
                raise ValueError("Cannot encrypt an empty or None message.")
            self.encryption_context.encrypt_message(message, key)
        except ValueError as e:
            return f"Error: {e}"

    def encrypt_list(self):
        message = ["Hello", 6]
        key = "1234"

        try:
            if isinstance(message, list):
                raise TypeError("Cannot encrypt a list.")
            self.encryption_context.encrypt_message(str(message), key)
        except TypeError as e:
            return f"Error: {e}"

    def encrypt_integer(self):
        message = 123
        key = "3567"

        try:
            if isinstance(message, int):
                raise ValueError("Cannot encrypt an integer; only strings are allowed.")
            self.encryption_context.encrypt_message(str(message), key)
        except ValueError as e:
            return f"Error: {e}"

    def decrypt_message_not_encrypted(self):
        encrypted_message = "nu80"
        key = "78"

        try:
            decrypted_message = self.encryption_context.decrypt_message(encrypted_message, key)
            if encrypted_message == decrypted_message:
                raise ValueError("The message appears to be not encrypted properly.")
        except ValueError as e:
            return f"Error: {e}"

    def decrypt_empty_message(self):
        encrypted_message = ""
        key = "3452"

        try:
            if not encrypted_message:
                raise ValueError("Cannot decrypt an empty message.")
            self.encryption_context.decrypt_message(encrypted_message, key)
        except ValueError as e:
            return f"Error: {e}"
