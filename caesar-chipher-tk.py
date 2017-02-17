#!/usr/bin/python3
# caesar-chiffre.py

from tkinter import *

def caesar(type, text, key):
    translated = ""

    if type == "decrypt":
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

    return translated

def encrypt():
    gettext = text.get("1.0",END)
    getkey = int(key.get("1.0",END))
    output.config(text=caesar("encrypt", gettext, getkey))

def decrypt():
    gettext = text.get("1.0",END)
    getkey = int(key.get("1.0",END))
    output.config(text=caesar("decrypt", gettext, getkey))

window = Tk()
window.wm_title("Caesar-Chiffre")

textlabel = Label(master=window,
                  font=("Arial", 14),
                  text="Text")
text = Text(master=window,
            font=("Arial", 14),
            width=40,
            height=7)
keylabel = Label(master=window,
                 font=("Arial", 14),
                 text="Key")
key = Text(master=window,
           font=("Arial", 14),
           width=40,
           height=3)
encrypt = Button(master=window,
                 font=("Arial", 14),
                 text="Encrypt",
                 command=encrypt)
decrypt = Button(master=window,
                 font=("Arial", 14),
                 text="Decrypt",
                 command=decrypt)
output = Label(master=window,
               font=("Arial", 14),
               text="Welcome to Caesar-Chiffre")

textlabel.pack()
text.pack()
keylabel.pack()
key.pack()
encrypt.pack(side=LEFT)
decrypt.pack(side=RIGHT)
output.pack()
window.mainloop()
