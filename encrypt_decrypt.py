def encrypt_caesar_cipher(file_path: str, shift: int) -> None:
    # Encrypts a text file using the Caesar cipher encryption algorithm

    with open(file_path, 'r') as file:
        text = file.read()
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    with open(file_path, 'w') as file:
        file.write(encrypted_text)


def decrypt_caesar_cipher(file_path: str, shift: int) -> None:
    # Decrypts a text file that was encrypted using the Caesar cipher encryption algorithm 

    with open(file_path, 'r') as file:
        text = file.read()
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    with open('decrypted_text.txt', 'w') as file:
        file.write(decrypted_text)


# Create a new text file called `text.txt`
with open('text.txt', 'w') as file:
    file.write('Hello, world!')

# Encrypt the contents in `text.txt` using key of 3
encrypt_caesar_cipher('text.txt', 4)

# Decrypt the encrypted text in `text.txt` using key of 3
decrypt_caesar_cipher('text.txt', 4)
