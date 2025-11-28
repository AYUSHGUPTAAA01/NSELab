def vigenere_encrypt(text, key):
    result = ""
    key = ''.join(ch for ch in key if ch.isalpha())
    key_length = len(key)
    key_int = [ord(i.lower()) - ord('a') for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = key_int[i % key_length]
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = ''.join(ch for ch in key if ch.isalpha())
    key_length = len(key)
    key_int = [ord(i.lower()) - ord('a') for i in key]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = key_int[i % key_length]
            result += chr((ord(char) - base - offset) % 26 + base)
        else:
            result += char
    return result

# Example usage
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", vigenere_decrypt(ciphertext, key))
