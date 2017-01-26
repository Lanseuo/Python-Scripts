#!/usr/bin/python3
# schere-stein-papier.py

from tkinter import *
from random import randint
import _thread
from time import sleep

punkte = [0, 0]
figuren = ["Schere", "Stein", "Papier"]
spielen = True
button_wait = False

def game():
    global button_wait
    label.config(text="Herzlich Willkommen zu Schere-Stein-Papier")
    while spielen:
        for runde in range(3):
            sleep(2)
            text_runde = "Runde " + str(runde + 1)
            label.config(text=text_runde)
            sleep(2)
            while button_wait == False:
                pass
            computer_choose()
            spielerfigur = choose_rb.get()
            check(spielerfigur, computerfigur)
            button_wait = False

        finish()
        punkte = [0, 0]

def button_pressed():
    global button_wait
    button_wait = True

def computer_choose():
    global computerfigur
    computerfigur = figuren[randint(0, 2)]
    label.config(text="Computer: " + computerfigur)
    sleep(1)


def check(a, b):
    if a == "Schere" or a == "schere":
        if b == "Schere" or b == "schere":
            result("ab")
        elif b == "Stein" or b == "stein":
            result("b")
        elif b == "Papier" or b == "papier":
            result("a")
    elif a == "Stein" or a == "stein":
        if b == "Schere" or b == "schere":
            result("a")
        elif b == "Stein" or b == "stein":
            result("ab")
        elif b == "Papier" or b == "papier":
            result("b")
    elif a == "Papier" or a == "papier":
        if b == "Schere" or b == "schere":
            result("b")
        elif b == "Stein" or b == "stein":
            result("a")
        elif b == "Papier" or b == "papier":
            result("ab")

def result(winner):
    global punkte
    if winner == "a":
        punkte[0] += 1
    elif winner == "ab":
        punkte[0] += 1
        punkte[1] += 1
    else:
        punkte[1] += 1
    label.config(text="Du: " + str(punkte[0]) + " & Computer: " + str(punkte[1]) + ".")
    pass


def finish():
    global spielen
    if punkte[0] > punkte[1]:
        label.config(text="Herzlichen Glückwunsch! Du hast gewonnen.")
    elif punkte[0] == punkte[1]:
        label.config(text="Gleichstand! Ihr habt beide gewonnen.")
    else:
        label.config(text="Schade! Leider hat der Computer gewonnen.")
    label.config(text="Noch eine Runde?")
    entscheidung = messagebox.askyesno(message="Noch eine Runde?")
    if entscheidung:
        spielen = True
    else:
        spielen = False


window = Tk()
window.wm_title("Schere-Stein-Papier")
label = Label(master=window,
              font=("Arial", 14),
              text="Herzlich Willkommen zu Schere-Stein-Papier")
choose_rb = StringVar(window)
schere_rb = Radiobutton(master=window,
                        text="Schere",
                        value="schere",
                        variable=choose_rb)
stein_rb = Radiobutton(master=window,
                       text="Stein",
                       value="stein",
                       variable=choose_rb)
papier_rb = Radiobutton(master=window,
                        text="Papier",
                        value="papier",
                        variable=choose_rb)
button = Button(master=window, text="Go", command=button_pressed)

_thread.start_new_thread(game, ())

label.pack()

schere_rb.pack()
stein_rb.pack()
papier_rb.pack()
button.pack()
window.mainloop()
