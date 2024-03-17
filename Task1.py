def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            shifted_char = char
        result += shifted_char

    if mode == 'encrypt':
        return result
    elif mode == 'decrypt':
        return caesar_cipher(result, -shift, 'encrypt')

def main():
    message = input("Enter the message to encrypt/decrypt: ")
    shift = int(input("Enter the shift value: "))
    action = input("Encrypt or Decrypt? (e/d): ")

    if action.lower() == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted message:", encrypted_message)
    elif action.lower() == 'd':
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
