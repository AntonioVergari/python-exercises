from packages.caesar_cipher.utils import char

def test_correct_input_switch_char():
    result = char.shift_char("a", 1)
    
    assert result == "b"

def test_correct_input_switch_num():
    result = char.shift_char("1",5)
    
    assert result == "6"
    
def test_invalid_input():
    try:
        char.shift_char("a", "b")
    except TypeError:
        result = TypeError
    
    assert result != None
