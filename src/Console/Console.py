from AesEncryption import AesEncryption
from EncryptionContext import EncryptionContext

def display_menu():
    print("Encryption System Menu")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    print()

def get_user_choice():
    choice = input("Select an option (1-3): ")
    return choice

def get_message_and_key():
    message = input("Enter the message: ")
    key = input("Enter the encryption key (must be 16 characters): ")
    return message, key

def main():
    encryption_strategy = AesEncryption()
    encryption_context = EncryptionContext(encryption_strategy)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            # Encrypt a message
            message, key = get_message_and_key()
            if len(key) != 16:
                print("Error: The key must be exactly 16 characters long.\n")
                continue

            encrypted_message = encryption_context.encrypt_message(message, key)
            print(f"Encrypted Message: {encrypted_message}\n")

        elif choice == "2":
            # Decrypt a message
            encrypted_message, key = get_message_and_key()
            if len(key) != 16:
                print("Error: The key must be exactly 16 characters long.\n")
                continue

            try:
                decrypted_message = encryption_context.decrypt_message(encrypted_message, key)
                print(f"Decrypted Message: {decrypted_message}\n")
            except Exception as e:
                print(f"Error: {str(e)}\n")

        elif choice == "3":
            print("Exiting the Encryption System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
