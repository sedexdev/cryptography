"""Vigenere Cipher implementation"""

ALPHABET = " abcdefghijklmnopqrstuvwxyz"
MESSAGE = "This is a test message"
KEY = "secretkey"


def encrypt(p_text, key) -> str:
    """
    Encryption algorithm to generate cipher text from <p_text>

    Args:
        p_text: str - plain text to encrypt
        key: str - private key
    Returns:
        str: encrypted cipher text
    """
    p_text = p_text.lower()

    cipher_text = ""
    key_index = 0

    for c in p_text:
        index = (ALPHABET.find(c) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text += ALPHABET[index]

        # increment private key index until we reach the end
        key_index += 1
        if key_index == len(key):
            # reset key index to start again
            key_index = 0

    return cipher_text


def decrypt(c_text, key) -> str:
    """
    Decryption algorithm to generate plain text from <c_text>

    Args:
        c_text: str - cipher text to decrypt
        key: str - private key
    Returns:
        str: decrypted plain text
    """
    c_text = c_text.lower()

    plain_text = ""
    key_index = 0

    for c in c_text:
        index = (ALPHABET.find(c) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text += ALPHABET[index]

        key_index += 1
        if key_index == len(key):
            key_index = 0

    return plain_text


def main() -> None:
    """
    Main function
    """

    encrypted_msg = encrypt(MESSAGE, KEY)
    print(encrypted_msg)
    print(decrypt(encrypted_msg, KEY))


if __name__ == "__main__":
    main()
