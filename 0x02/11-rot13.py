#!/usr/bin/python3
# a module that implement rot 13 encryption and decryption

def rot13(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord("a")+13) % 26 + ord("a"))
        elif char.isupper():
            result += chr((ord(char) - ord("A")+13) % 26 + ord("A"))
        else:
            result += char
    return result


if __name__ == "__main__":
    message = input("Enter a message: ")
    print("Rot13 Encoded/Decoded message:", rot13(message))
    

