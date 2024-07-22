"""Caesar Cipher implementation"""

# import matplotlib.pylab as plt
import py3langid.langid as plid

# constants
ALPHABET = " abcdefghijklmnopqrstuvwxyz"
MESSAGE = "This is a test message"
MESSAGE_2 = """
Language is meant to be a playful, ever-shifting creation but we have been taught, and most
of us continue to believe, that language must obediently follow precisely prescribed rules
that govern clear sentence structures, specific word orders, correct spellings, and proper
pronunciations. If you make a mistake or step out of bounds there are countless, self-appointed
language experts who will promptly push you back into safe terrain and scold you for your errors.
And in case you need reminding, there are hundreds of dictionaries and grammar books to ensure
that you remember the “right” way to use English.
"""


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
        identifier = plid.LanguageIdentifier.from_pickled_model(
            plid.MODEL_FILE, norm_probs=True
        )
        lang, prob = identifier.classify(plain_text)
        if lang == "en" and prob >= 0.95:
            return i
    return -1


def freq_analysis(c_text) -> int:
    """
    Frequency analysis cracking algorithm to find encryption key

    Args:
        c_text: str - cipher text to crack
    Returns:
        int: encryption key
    """
    letter_count = {}

    for letter in ALPHABET:
        letter_count[letter] = 0

    for c in c_text:
        if c.isalpha() or c.isspace():
            letter_count[c] += 1

    # the lines below show a plotted graph of the frequency of letters in c_text

    # plt.bar(letter_count.keys(), letter_count.values())
    # plt.show()

    sorted_by_value = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # this calculation is known to find encryption key values
    # based on the numerical difference between the most common
    # letter in a given text and 'e'
    key = ALPHABET.find(sorted_by_value[1][0]) - (ALPHABET.find("e"))
    return key


def main() -> None:
    """
    Main function
    """

    encrypted_msg = encrypt(MESSAGE, 3)
    decrypted_msg = decrypt(encrypted_msg, 3)

    print(encrypted_msg)
    print(decrypted_msg)

    print(brute_force(encrypted_msg))

    encrypted_msg = encrypt(MESSAGE_2, 8)
    print(freq_analysis(encrypted_msg))


if __name__ == "__main__":
    main()
