"""Caesar Cipher implementation"""

# constants
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3
MESSAGE = "This is a test message"


def encrypt(p_text) -> str:
    """
    Encryption algorithm that shifts the plain text
    characters right <KEY> times.

    Args:
        p_text: str - plain text to encrypt
    Returns:
        str: encrypted cipher text
    """
    cipher_text = ""
    p_text = p_text.upper()

    for c in p_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text += ALPHABET[index]

    return cipher_text


def decrypt(c_text) -> str:
    """
    Decryption algorithm that shifts the cipher text
    characters left <KEY> times.

    Args:
        c_text: str - cipher text to decrypt
    Returns:
        str: decrypted plain text
    """
    plain_text = ""

    for c in c_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text += ALPHABET[index]

    return plain_text


def main() -> None:
    """
    Main function
    """
    encrypted_msg = encrypt(MESSAGE)
    decrypted_msg = decrypt(encrypted_msg)

    print(encrypted_msg)
    print(decrypted_msg)


if __name__ == "__main__":
    main()
