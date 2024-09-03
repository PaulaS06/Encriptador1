import EncryptionSystem
import Tests.EncryptionSystem_Test

class ErrorsAndExceptions:
    #errores encriptado
    def encrypt_without_key(self):
        message = "Hola Como Estas"
        key = ""

        try:
            if not key:
                raise KeyError("El mensaje no puede encriptar sin clave")
        # Aquí iría el resto del código de cifrado
        except KeyError as e:
            print(f"Error: {e}")

    def encrypt_empty_message(self):
        massage = "" or None
        key = "123"

        try:
            if not massage:
                raise ValueError("El mensaje no puede estar vacío o ser None")
        # Aquí iría el resto del código de cifrado
        except ValueError as e:
            print(f"Error: {e}")

    def encrypt_list(self):
        message = ["Hola", 6]
        key = "1234"

        try:
            if message == list:
                raise TypeError("No se puede encriptar una lista")
        # Aquí iría el resto del código de cifrado
        except TypeError as e:
            print(f"Error: {e}")

    def encrypt_integer(self):
        message = 123
        key = "3567"

        try:
            if message == int:
                raise ValueError("El mensaje no puede encriptar un entero, ni otro tipo de dato que no sea un string")
        # Aquí iría el resto del código de cifrado
        except ValueError as e:
            print(f"Error: {e}")


    #errores de desencriptado.
    def decrypt_message_not_encrypted(self):
        message = "nu80"
        key = "78"
        mensaje_descifrado = "No se puede descifrar"

        try:
            # Simulamos la verificación de si el mensaje está cifrado
            if not message.esta_cifrado(message):
                raise IndexError("El mensaje no está cifrado")
            # Aquí iría el código real de descifrado si el mensaje estuviera cifrado
        except IndexError as e:
            print(f"Error: {e}")
            mensaje_descifrado = "No se puede descifrar"

            print(f"Mensaje descifrado: {mensaje_descifrado}")

    def decrypt_empty_key(self):
        message = "cYPKAEiAO1kzbWOZDODyv3GDygBIgDtZM21jmQzg8r9xg8oASIA7WTNtY5kM4PK"
        key = ""
        mensaje_descifrado = "No se puede descifrar"

        try:
            if not key:
                raise KeyError("La clave no puede estar vacía")
            # Aquí iría el código real de descifrado si la clave no estuviera vacía
        except KeyError as e:
            print(f"Error: {e}")
            mensaje_descifrado = "No se puede descifrar"

            print(f"Mensaje descifrado: {mensaje_descifrado}")

    def decrypt_partially_encrypted_message(self):
        message = "xWTdQjgVKprNBiw"
        key = "789"
        mensaje_descifrado = "No se puede descifrar"

        try:
            if len(message) < 20:  # Ejemplo de condición para un mensaje parcialmente cifrado
                raise IndexError("El mensaje está parcialmente cifrado o es demasiado corto")
        # Aquí iría el código real de descifrado si el mensaje no estuviera parcialmente cifrado
        except IndexError as e:
            print(f"Error: {e}")
            mensaje_descifrado = "No se puede descifrar"

            print(f"Mensaje descifrado: {mensaje_descifrado}")

    def decrypt_empty_message(self):
        message = ""
        key = "3452"
        mensaje_descifrado = "No se puede descifrar"

        try:
            if not message:
                raise ValueError("El mensaje no puede estar vacío")
        # Aquí iría el código real de descifrado si el mensaje no estuviera vacío
        except ValueError as e:
            print(f"Error: {e}")
            mensaje_descifrado = "No se puede descifrar"

            print(f"Mensaje descifrado: {mensaje_descifrado}")