def encrypt(plaintext, key):
    encrypted = ""
    for i, char in enumerate(plaintext):
        encrypted += chr(ord(char) ^ ord(key[i % len(key)]))
    return encrypted

def decrypt(encrypted, key):
    plaintext = ""
    for i, char in enumerate(encrypted):
        plaintext += chr(ord(char) ^ ord(key[i % len(key)]))
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted = encrypt(plaintext, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)