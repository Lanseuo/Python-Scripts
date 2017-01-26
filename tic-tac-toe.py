#!/usr/bin/python3
# tic-tac-toe.py

from random import *

play = True

def printGrid():
    grid = "-------------" + "\n" + \
       "| " + a + " | " + b + " | " + c + " | " + "\n" + \
       "| " + d + " | " + e + " | " + f + " | " + "\n" + \
       "| " + g + " | " + h + " | " + i + " | " + "\n" + \
       "-------------"
    return grid

def init():
    global play, not_used, player_symbol, computer_symbol, a, b, c, d, e, f, g, h, i
    a = "A"
    b = "B"
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    h = "H"
    i = "I"
    play = True
    not_used = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    print("* Tic-Tac-Toe *")
    print("What do you want to be?")
    player_symbol = ""
    while player_symbol not in ["X", "O"]:
        player_symbol = input("X or O? ")
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

def tick(field):
    global player_symbol, not_used, a, b, c, d, e, f, g, h, i
    field = field.lower()
    if field in not_used:
        not_used.remove(str(field))
        if field == "a":
            a = player_symbol
        elif field == "b":
            b = player_symbol
        elif field == "c":
            c = player_symbol
        elif field == "d":
            d = player_symbol
        elif field == "e":
            e = player_symbol
        elif field == "f":
            f = player_symbol
        elif field == "g":
            g = player_symbol
        elif field == "h":
            h = player_symbol
        elif field == "i":
            i = player_symbol
    else:
        print("This field is already ticked")

def computer_choose():
    global not_used, compute_symbol, a, b, c, d, e, f, g, h, i
    choose = choice(not_used)
    print("Computer: " + choose.upper())
    not_used.remove(str(choose))
    if choose == "a":
        a = computer_symbol
    elif choose == "b":
        b = computer_symbol
    elif choose == "c":
        c = computer_symbol
    elif choose == "d":
        d = computer_symbol
    elif choose == "e":
        e = computer_symbol
    elif choose == "f":
        f = computer_symbol
    elif choose == "g":
        g = computer_symbol
    elif choose == "h":
        h = computer_symbol
    elif choose == "i":
        i = computer_symbol

def check():
    global a, b, c, d, e, f, g, h, i
    for element in ["X", "Y"]:
        if a == element and b == element and c == element:
            result(element)
        if d == element and e == element and f == element:
            result(element)
        if g == element and h == element and i == element:
            result(element)
        if a == element and d == element and g == element:
            result(element)
        if b == element and e == element and h == element:
            result(element)
        if c == element and f == element and i == element:
            result(element)
        if a == element and e == element and i == element:
            result(element)
        if c == element and e == element and g == element:
            result(element)

def result(who):
    global player_symbol, computer_symbol, play
    print(printGrid())
    if who == player_symbol:
        print("Congratulations. You're the winner.")
    else:
        print("Dammage. The computer won.")
    print("One more time?")
    again = "XyZ"
    while again not in ["Y", "N", "y", "n"]:
        again = input("Y/N: ")
    if again == "Y" or again == "y":
        play = True
    else:
        play = False


if __name__ == "__main__":
    init()
    while play:
        print(printGrid())
        check()
        tick(input("Letter: "))
        check()
        computer_choose()