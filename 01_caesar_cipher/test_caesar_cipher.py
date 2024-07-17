from caesar_cipher import decrypt, encrypt


class TestCaesarCipher:
    def test_encrypt_empty(self) -> None:
        assert encrypt('') == ''

    def test_encrypt(self) -> None:
        assert encrypt('This is a test message') == 'WKLVCLVCDCWHVWCPHVVDJH'

    def test_decrypt_empty(self) -> None:
        assert decrypt('') == ''

    def test_decrypt(self) -> None:
        assert decrypt('WKLVCLVCDCWHVWCPHVVDJH') == 'THIS IS A TEST MESSAGE'
