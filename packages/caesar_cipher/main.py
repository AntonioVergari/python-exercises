import sys
sys.path.append('packages')
from crypt.decrypt import decrypt
from crypt.encrypt import encrypt


print("Welcome to caesar cipher")
exit = False
while not exit :
    
    operation = input("what do you want to do? Choose between encrypt and decrypt. or write quit to end the program ").lower()

    if operation== "encrypt":
        text = input("insert the text to encrypt ")
        shift = int(input("insert the numer of positions to shift "))
        print("encrypt in progress...")
        result = encrypt(text,shift)
        print(f"the result is {result}")
    elif operation == "decrypt":
        text = input("insert the text to decrypt")
        shift = int("insert the numer of positions to shift")
        print("decrypt in progress...")
        result = decrypt(text,shift)
        print(f"the result is {result}")
    elif operation == "exit":
        print("Thanks for using caesar cipher")
        exit = True
    else:
        print("Invalid choice. Please retry")