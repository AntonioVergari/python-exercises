from packages.caesar_cipher.utils import char

def encrypt(unecrypted_string, decrypt_shift):
    """
    decrypt a string using caesar's cipher
    
    Args:
        unecrypted_string(str): the unencrypted text that should be encrypted
        decrypt_shift(int): the number of char to shift
    
    Returns:
        str: the encrypted text
    """
    result = ""
    for encrypted_char in unecrypted_string:
        result += char.shift_char(encrypted_char, decrypt_shift)
        
    return result