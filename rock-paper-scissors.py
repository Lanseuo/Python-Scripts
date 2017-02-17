#!/usr/bin/python3
# rock-paper-scissors.py

from random import randint

points = [0, 0]
figures = ["Rock", "Paper", "Scissors"]
play = True

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
    print("You: " + str(points[0]) + " & Computer: " + str(points[1]) + ".")

def finish():
    global play
    if points[0] > points[1]:
        print("Congratulations! You're the winner.")
    elif points[0] == points[1]:
        print("Tie! Both of you won.")
    else:
        print("Damage! Unfortunately the computer won.")
    print("Again?")
    decision = 0
    while decision not in ["Yes", "No", "yes", "no"]:
        decision = input("Yes / No: ")
    if decision == "Yes" or decisionde == "yes":
        play = True
    else:
        play = False

while play:
    print("* Rock-Paper-Scissors *")

    for runde in range(3):
        print("Runde " + str(runde + 1) + ":")
        player = 0
        while player not in ["Rock", "Scissors", "Paper", "rock", "scissors",  "paper"]:
            player = input("Your choice: ")
        computer = figures[randint(0, 2)]
        print("Computer: " + computer)
        check(player, computer)

    finish()
    punkte = [0, 0]