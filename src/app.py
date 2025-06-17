# Note: Requires 'pycryptodome' library. Install with: pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

def caesar_cipher_func(message, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def vigenere_cipher_func(message, keyword, mode='encrypt'):
    keyword = ''.join(filter(str.isalpha, keyword.upper()))
    if not keyword:
        return "Error: Keyword must contain at least one letter"
    key_stream = [ord(k) - ord('A') for k in keyword]
    result = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shift = key_stream[key_index % len(key_stream)]
            if mode == 'decrypt':
                shift = -shift
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            key_index += 1
        else:
            result += char
    return result


def caesar_cipher():
    while True:
        print("\n=== Caesar Cipher ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Back to main menu")
        choice = input("Select an option (1-3): ")
        if choice in ['1', '2']:
            mode = 'encrypt' if choice == '1' else 'decrypt'
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift value (e.g., 3): "))
                result = caesar_cipher_func(message, shift, mode)
                print(f"\nResult: {result}")
            except ValueError:
                print("Error: Shift must be an integer")
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")


def vigenere_cipher():
    while True:
        print("\n=== Vigenère Cipher ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Back to main menu")
        choice = input("Select an option (1-3): ")
        if choice in ['1', '2']:
            mode = 'encrypt' if choice == '1' else 'decrypt'
            message = input("Enter your message: ")
            keyword = input("Enter keyword (letters only): ")
            result = vigenere_cipher_func(message, keyword, mode)
            print(f"\nResult: {result}")
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")

def aes_encryption():
    while True:
        print("\n=== AES Encryption ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Back to main menu")
        choice = input("Select an option (1-3): ")
        if choice == '1':
            message = input("Enter message to encrypt: ")
            key = get_random_bytes(16)
            cipher = AES.new(key, AES.MODE_CBC)
            iv = cipher.iv
            ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
            print("\nEncryption complete!")
            print(f"Ciphertext (hex): {ciphertext.hex()}")
            print(f"Key (hex): {key.hex()}")
            print(f"IV (hex): {iv.hex()}")
            print("Save these values for decryption!")
        elif choice == '2':
            try:
                ciphertext_hex = input("Enter ciphertext (hex): ")
                key_hex = input("Enter key (hex): ")
                iv_hex = input("Enter IV (hex): ")
                ciphertext = bytes.fromhex(ciphertext_hex)
                key = bytes.fromhex(key_hex)
                iv = bytes.fromhex(iv_hex)
                cipher = AES.new(key, AES.MODE_CBC, iv=iv)
                plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
                print(f"\nDecrypted message: {plaintext.decode()}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")


def hashing():
    print("\n=== SHA-256 Hashing ===")
    message = input("Enter message to hash: ")
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    print(f"\nHash: {hash_value}")

def rsa_signatures():
    private_key = None
    public_key = None
    while True:
        print("\n=== RSA Digital Signatures ===")
        print("1. Generate RSA key pair")
        print("2. Sign a message")
        print("3. Verify a signature")
        print("4. Back to main menu")
        choice = input("Select an option (1-4): ")
        if choice == '1':
            key = RSA.generate(2048)
            private_key = key
            public_key = key.publickey()
            print("\nRSA key pair generated successfully!")
        elif choice == '2':
            if private_key is None:
                print("Error: Generate a key pair first")
                continue
            message = input("Enter message to sign: ")
            h = SHA256.new(message.encode())
            signature = pkcs1_15.new(private_key).sign(h)
            print(f"\nSignature (hex): {signature.hex()}")
        elif choice == '3':
            if public_key is None:
                print("Error: Generate a key pair first")
                continue
            message = input("Enter original message: ")
            signature_hex = input("Enter signature (hex): ")
            try:
                signature = bytes.fromhex(signature_hex)
                h = SHA256.new(message.encode())
                pkcs1_15.new(public_key).verify(h, signature)
                print("\nSignature is valid!")
            except (ValueError, TypeError):
                print("\nSignature is invalid")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")


def main():
    while True:
        print("\n" + "="*40)
        print("   Welcome to the Cryptography Toolkit   ")
        print("="*40)
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. AES Encryption")
        print("4. SHA-256 Hashing")
        print("5. RSA Digital Signatures")
        print("6. Exit")
        choice = input("\nChoose a method (1-6): ")
        print("="*40)
        
        if choice == '1':
            caesar_cipher()
        elif choice == '2':
            vigenere_cipher()
        elif choice == '3':
            aes_encryption()
        elif choice == '4':
            hashing()
        elif choice == '5':
            rsa_signatures()
        elif choice == '6':
            print("\nThank you for using the Cryptography Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if _name_ == "_main_":
    main()
