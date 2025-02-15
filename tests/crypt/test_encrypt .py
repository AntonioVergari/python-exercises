from packages.caesar_cipher.crypt import encrypt

def test_encript():
    text_to_encrypt = "a a"
    encrypt_shift = 1
    
    result = encrypt.encrypt(text_to_encrypt, encrypt_shift)
    
    assert result == "b!b"