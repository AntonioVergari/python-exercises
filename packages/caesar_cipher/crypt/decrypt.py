from caesar_cipher.utils import char

def decrypt(encrypted_string, decrypt_shift):
    """
    decrypt a string using caesar's cipher
    
    Args:
        encrypted_string(str): the encrypted text that should be decrypted
        decrypt_shift(int): the number of char to shift
    
    Returns:
        str: the decrypted text
    """
    result = ""
    for encrypted_char in encrypted_string:
        result += char.shift_char(encrypted_char, -decrypt_shift)
        
    return result