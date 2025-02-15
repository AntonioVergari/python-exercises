from packages.caesar_cipher.crypt import decrypt

def test_decript():
    encrypted_text = "b!b"
    decrypt_shift = 1
    
    result = decrypt.decrypt(encrypted_text, decrypt_shift)
    
    assert result == "a a"