class EncryptionContext:
    """Context to use the selected encryption strategy."""
    def __init__(self, strategy):
        self.strategy = strategy

    def encrypt_message(self, message: str, key: str) -> str:
        key_bytes = self._key_to_bytes(key)
        return self.strategy.encrypt(message, key_bytes)

    def decrypt_message(self, encrypted_message: str, key: str) -> str:
        key_bytes = self._key_to_bytes(key)
        return self.strategy.decrypt(encrypted_message, key_bytes)

    def _key_to_bytes(self, key: str) -> bytes:
        return key.encode('utf-8').ljust(16)[:16]
