"""Caesar Cipher test cases"""

from caesar_cipher import decrypt, encrypt


class TestCaesarCipher:
    """
    Test class for Caesar Cipher functions
    """
    
    def test_encrypt_empty(self) -> None:
        """
        Test empty string encryption
        """
        assert encrypt("") == ""

    def test_encrypt(self) -> None:
        """
        Test message encrypts correctly
        """
        assert encrypt("This is a test message") == "WKLVCLVCDCWHVWCPHVVDJH"

    def test_decrypt_empty(self) -> None:
        """
        Test empty string decryption
        """
        assert decrypt("") == ""

    def test_decrypt(self) -> None:
        """
        Test message decrypts correctly
        """
        assert decrypt("WKLVCLVCDCWHVWCPHVVDJH") == "THIS IS A TEST MESSAGE"
