#!/usr/bin/python3
# rock-paper-scissors-tk.py

from tkinter import *
from random import randint
import _thread
from time import sleep

points = [0, 0]
figures = ["Rock", "Paper", "Scissors"]
play = True
button_wait = False

def game():
    global button_wait, points
    label.config(text="Rock-Paper-Scissors")
    while play:
        for round in range(3):
            sleep(2)
            text_round = "Round " + str(round + 1)
            label.config(text=text_round)
            sleep(2)
            while button_wait == False:
                pass
            computer_choose()
            playerfigure = choose_rb.get()
            check(playerfigure, computerfigure)
            button_wait = False

        finish()
        points = [0, 0]

def button_pressed():
    global button_wait
    button_wait = True

def computer_choose():
    global computerfigure
    computerfigure = figures[randint(0, 2)]
    label.config(text="Computer: " + computerfigure)
    sleep(1)


def check(a, b):
    if a == "Scissors" or a == "scissors":
        if b == "Scissors" or b == "scissors":
            result("ab")
        elif b == "Rock" or b == "rock":
            result("b")
        elif b == "Paper" or b == "paper":
            result("a")
    elif a == "Rock" or a == "rock":
        if b == "Scissors" or b == "scissors":
            result("a")
        elif b == "Rock" or b == "rock":
            result("ab")
        elif b == "Paper" or b == "paper":
            result("b")
    elif a == "Paper" or a == "paper":
        if b == "Scissors" or b == "scissors":
            result("b")
        elif b == "Rock" or b == "rock":
            result("a")
        elif b == "Paper" or b == "paper":
            result("ab")

def result(winner):
    global points
    if winner == "a":
        points[0] += 1
    elif winner == "ab":
        points[0] += 1
        points[1] += 1
    else:
        points[1] += 1
    label.config(text="You: " + str(points[0]) + " & Computer: " + str(points[1]) + ".")
    pass


def finish():
    global play
    if points[0] > points[1]:
        label.config(text="Congratulations! You're the winner.")
    elif points[0] == points[1]:
        label.config(text="Tie! Both of you won.")
    else:
        label.config(text="Damage! Unfortunately the computer won.")
    label.config(text="Again?")
    decision = messagebox.askyesno(message="Again?")
    if decision:
        play = True
    else:
        play = False


window = Tk()
window.wm_title("Rock-Paper-Scissors")
label = Label(master=window,
              font=("Arial", 14),
              text="Rock-Paper-Scissors")
choose_rb = StringVar(window)
scissors_rb = Radiobutton(master=window,
                          text="Scissors",
                          value="Scissors",
                          variable=choose_rb)
rock_rb = Radiobutton(master=window,
                      text="Rock",
                      value="rock",
                      variable=choose_rb)
paper_rb = Radiobutton(master=window,
                       text="Paper",
                       value="paper",
                       variable=choose_rb)
button = Button(master=window, text="Go", command=button_pressed)

_thread.start_new_thread(game, ())

label.pack()

scissors_rb.pack()
rock_rb.pack()
paper_rb.pack()
button.pack()
window.mainloop()
