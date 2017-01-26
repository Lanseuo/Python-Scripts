#!/usr/bin/python3
# schere-stein-papier.py

from random import randint

punkte = [0, 0]
figuren = ["Schere", "Stein", "Papier"]
spielen = True

def check(a, b):
    if a == "Schere" or a == "schere":
        if b == "Schere" or b == "schere":
            result("ab")
        elif b == "Stein" or b == "stein":
            result("b")
        elif b == "Papier" or b == "papier":
            result("a")
        else:
            print("Spieler B muss Schere, Stein oder Papier wählen!")
    elif a == "Stein" or a == "stein":
        if b == "Schere" or b == "schere":
            result("a")
        elif b == "Stein" or b == "stein":
            result("ab")
        elif b == "Papier" or b == "papier":
            result("b")
        else:
            print("Spieler B muss Schere, Stein oder Papier wählen!")
    elif a == "Papier" or a == "papier":
        if b == "Schere" or b == "schere":
            result("b")
        elif b == "Stein" or b == "stein":
            result("a")
        elif b == "Papier" or b == "papier":
            result("ab")
        else:
            print("Spieler B muss Schere, Stein oder Papier wählen!")
    else:
        print("Spieler A muss Schere, Stein oder Papier wählen!")

def result(winner):
    global punkte
    if winner == "a":
        punkte[0] += 1
    elif winner == "ab":
        punkte[0] += 1
        punkte[1] += 1
    else:
        punkte[1] += 1
    print("Du: " + str(punkte[0]) + " & Computer: " + str(punkte[1]) + ".")
    pass

def finish():
    global spielen
    if punkte[0] > punkte[1]:
        print("Herzlichen Glückwunsch! Du hast gewonnen.")
    elif punkte[0] == punkte[1]:
        print("Gleichstand! Ihr habt beide gewonnen.")
    else:
        print("Schade! Leider hat der Computer gewonnen.")
    print("Noch eine Runde?")
    entscheidung = 0
    while entscheidung not in ["Ja", "Nein", "ja", "nein"]:
        entscheidung = input("Ja / Nein: ")
    if entscheidung == "Ja" or entscheidung == "ja":
        spielen = True
    else:
        spielen = False

while spielen:
    print("* Schere-Stein-Papier *")

    for runde in range(3):
        print("Runde " + str(runde + 1) + ":")
        spielerfigur = 0
        while spielerfigur not in ["Schere", "Stein", "Papier", "schere", "stein", "papier"]:
            spielerfigur = input("Deine Wahl: ")
        computerfigur = figuren[randint(0, 2)]
        print("Computer: " + computerfigur)
        check(spielerfigur, computerfigur)

    finish()
    punkte = [0, 0]