"""Vigenere Cipher test cases"""


from vigenere_cipher.cipher import MESSAGE, decrypt, encrypt


class TestVigenereCipher:
    """
    Test class for Vigenere Cipher functions
    """

    def test_encrypt_empty(self) -> None:
        """Test encrypting empty string returns empty string"""
        assert encrypt("", "testing") == ""

    def test_encrypt(self) -> None:
        """Test encryption algorithm returns correct result"""
        assert encrypt(MESSAGE, "testing") == "mmaliwztfsmnf trxlaony"

    def test_decrypt_empty(self) -> None:
        """Test decrypting empty string returns empty string"""
        assert decrypt("", "testing") == ""

    def test_decrypt(self) -> None:
        """Test decryption algorithm returns correct result"""
        assert decrypt("mmaliwztfsmnf trxlaony", "testing") == MESSAGE.lower()
