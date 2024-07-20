"""Caesar Cipher implementation"""

from py3langid.langid import MODEL_FILE, LanguageIdentifier

# constants
ALPHABET = " abcdefghijklmnopqrstuvwxyz"
MESSAGE = "This is a test message"


def encrypt(p_text, key) -> str:
    """
    Encryption algorithm that shifts the plain text
    characters right <key> times.

    Args:
        p_text: str - plain text to encrypt
        key:    int - symmetric key
    Returns:
        str: encrypted cipher text
    """
    cipher_text = ""
    p_text = p_text.lower()

    for c in p_text:
        index = ALPHABET.find(c)
        index = (index + key) % len(ALPHABET)
        cipher_text += ALPHABET[index]

    return cipher_text


def decrypt(c_text, key) -> str:
    """
    Decryption algorithm that shifts the cipher text
    characters left <key> times.

    Args:
        c_text: str - cipher text to decrypt
        key:    int - symmetric key
    Returns:
        str: decrypted plain text
    """
    plain_text = ""

    for c in c_text:
        index = ALPHABET.find(c)
        index = (index - key) % len(ALPHABET)
        plain_text += ALPHABET[index]

    return plain_text


def brute_force(c_text) -> int:
    """
    Brute force cracking algorithm to find encryption key

    Args:
        c_text: str - cipher text to crack
    Returns:
        int: encryption key
    """
    for i in range(len(ALPHABET)):
        plain_text = decrypt(c_text, i)
        identifier = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)
        lang, prob = identifier.classify(plain_text)
        if lang == "en" and prob >= 0.95:
            return i
    return -1


def main() -> None:
    """
    Main function
    """

    encrypted_msg = encrypt(MESSAGE, 3)
    decrypted_msg = decrypt(encrypted_msg, 3)

    print(encrypted_msg)
    print(decrypted_msg)

    print(brute_force(encrypted_msg))


if __name__ == "__main__":
    main()
