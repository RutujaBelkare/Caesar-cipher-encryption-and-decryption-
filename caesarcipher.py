# Python program to encrypt and decrypt text using the Caesar cipher algorithm

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    print("Caesar Cipher Algorithm")
    while True:
        mode = input("Choose an option (encrypt, decrypt, exit): ").strip().lower()
        if mode == "exit":
            print("Exiting the program. Goodbye!")
            break
        elif mode in ["encrypt", "decrypt"]:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value (integer): "))
            if mode == "encrypt":
                result = caesar_cipher_encrypt(text, shift)
                print(f"Encrypted text: {result}")
            else:
                result = caesar_cipher_decrypt(text, shift)
                print(f"Decrypted text: {result}")
        else:
            print("Invalid option. Please choose 'encrypt', 'decrypt', or 'exit'.")