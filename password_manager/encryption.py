SHIFT = 33

def encrypt(password):

    encrypted = ""

    for char in password:

        if char.isalpha():
            # Shift the character by the specified amount
            shifted = chr((ord(char) - 97 + SHIFT) % 26 + 97)
            encrypted += shifted

        else:
            # Non-alphabetic characters are not shifted
            encrypted += char

    return encrypted


def decrypt(password):

    decrypted = ""

    for char in password:

        if char.isalpha():
            # Shift the character back by the specified amount
            shifted = chr((ord(char) - 97 - SHIFT) % 26 + 97)
            decrypted += shifted

        else:
            # Non-alphabetic characters are not shifted
            decrypted += char

    return decrypted
