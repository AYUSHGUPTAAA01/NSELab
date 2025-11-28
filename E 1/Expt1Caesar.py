def caesar_encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage
plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))
ciphertext = caesar_encrypt(plaintext, shift)
print("Encrypted:", ciphertext)
print("Decrypted:", caesar_decrypt(ciphertext, shift))
