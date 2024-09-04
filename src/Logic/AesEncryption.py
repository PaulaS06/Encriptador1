from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class AesEncryption:
    """Concrete implementation using AES encryption."""
    def __init__(self, block_size: int = 16):
        self.block_size = block_size

    def encrypt(self, message: str, key: bytes) -> str:
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_bytes = cipher.encrypt(pad(message.encode('utf-8'), self.block_size))
        return base64.b64encode(cipher.iv + encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_message: str, key: bytes) -> str:
        encrypted_data = base64.b64decode(encrypted_message)
        iv = encrypted_data[:self.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_data[self.block_size:]), self.block_size)
        return decrypted_bytes.decode('utf-8')
