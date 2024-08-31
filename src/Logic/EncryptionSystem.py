from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util.Padding import pad, unpad
import base64


class SystemEncryption:
    def __init__(self, key):
        self.key = MD5.new(key.encode()).digest()
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, message):
        message_bytes = message.encode()
        padded_message = pad(message_bytes, AES.block_size)
        encrypted_message = self.cipher.encrypt(padded_message)
        return base64.b64encode(encrypted_message).decode()

    def decrypt(self, encrypted_message):
        encrypted_message_bytes = base64.b64decode(encrypted_message)
        decrypted_message = self.cipher.decrypt(encrypted_message_bytes)
        message = unpad(decrypted_message, AES.block_size).decode()
        return message


def esta_cifrado(mensaje_cifrado):
    pass
