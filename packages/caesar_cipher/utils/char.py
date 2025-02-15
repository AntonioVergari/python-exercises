def shift_char(char:str, shift:int):
    """
    shift the ascii of the char by the number in shift
    
    Args:
        char(str): the char to shift
        shift(int): the number of shift to apply at the char
        
    Returns:
        str: a shifted char
    """
    #get ascii value
    ascii = ord(char)
    
    return chr(ascii + shift)