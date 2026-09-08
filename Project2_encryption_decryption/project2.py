while True:
    message = input("Enter a message to Encrypt: ")
    shift = int(input("Enter your Desired Shift Key (a number): "))

    encrypted = ""

    for char in message:
        if char .isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted = encrypted + new_char
        elif char .islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted = encrypted + new_char
        else:
            encrypted = encrypted + char

    print("Encrypted message:", encrypted) 

    decrypted = ""

    for char in encrypted:
        if char.isupper():
            new_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted = decrypted + new_char 
        elif char .islower():
                new_char = chr((ord(char) - 97 - shift) % 26 + 97)
                decrypted = decrypted + new_char
        else:
            decrypted = decrypted + char  

    print("Decrypted message:", decrypted)

    again = input("Encrypt another message? (yes/no): ")
    if again.lower() != "yes":
         break