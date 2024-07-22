"""Caesar Cipher test cases"""

from cipher import MESSAGE_2, brute_force, decrypt, encrypt, freq_analysis


class TestCaesarCipher:
    """
    Test class for Caesar Cipher functions
    """

    def test_encrypt_empty(self) -> None:
        """
        Test empty string encryption
        """
        assert encrypt("", 0) == ""

    def test_encrypt(self) -> None:
        """
        Test message encrypts correctly
        """
        assert encrypt("This is a test message", 3) == "wklvclvcdcwhvwcphvvdjh"

    def test_decrypt_empty(self) -> None:
        """
        Test empty string decryption
        """
        assert decrypt("", 0) == ""

    def test_decrypt(self) -> None:
        """
        Test message decrypts correctly
        """
        assert decrypt("wklvclvcdcwhvwcphvvdjh", 3) == "this is a test message"

    def test_crack_brute_force(self) -> None:
        """
        Test brute force cracking algorithm returns correct key
        """
        assert brute_force("wklvclvcdcwhvwcphvvdjh") == 3

    def test_crack_frequency_analysis(self) -> None:
        """
        Test frequency analysis cracking algorithm returns correct key
        """
        cipher_text = encrypt(MESSAGE_2, 7)
        key_crack = freq_analysis(cipher_text) 
        assert 6 <= key_crack <= 8
