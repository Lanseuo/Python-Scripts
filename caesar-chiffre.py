#!/usr/bin/python3
# caesar-chiffre.py

def caesar(type, text, key):
    translated = ""
    text = text.lower()

    if type == "d" or type == "D" or type == "decrypt" or type == "Decrypt":
        key = -key

    for symbol in text:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

            translated += chr(num)

        else:
            translated += symbol

    return "Message: " + translated


print("Welcome to Caesar Cipher")
while True:
    type = input("Encrypt or Decrypt: ")
    text = input("Text: ")
    key = int(input("Key: "))
    print(caesar(type, text, key))