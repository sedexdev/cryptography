"""Caesar Cipher test cases"""

from caesar_cipher import (
    brute_force,
    decrypt,
    encrypt
)


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
