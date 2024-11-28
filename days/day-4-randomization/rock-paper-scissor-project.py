import random
from random import choice

import asciiArt

choices = ["rock", "paper", "scissors"]

print("[0] - Rock\n[1] - Paper\n[2] - Scissors?")
playerChoice = int(input("Enter choice: "))
computerChoice = random.choice(choices)
isPlayerWinner = True

if computerChoice == "rock":

    if playerChoice == 0 :
        print("\nYou chose:")
        print(asciiArt.rock)

        print("\nComputer chose :")
        print(asciiArt.rock)

        isPlayerWinner = False

        print(asciiArt.draw)

    elif playerChoice == 1 :
        print("\nYou chose:")
        print(asciiArt.paper)

        print("\nComputer chose :")
        print(asciiArt.rock)

        isPlayerWinner = True

    elif playerChoice == 2 :
        print("\nYou chose:")
        print(asciiArt.scissors)

        print("\nComputer chose :")
        print(asciiArt.rock)

        isPlayerWinner = False

elif computerChoice == "paper":

    if playerChoice == 0:
        print("\nYou chose:")
        print(asciiArt.rock)

        print("\nComputer chose :")
        print(asciiArt.paper)

        isPlayerWinner = False

    elif playerChoice == 1:
        print("\nYou chose:")
        print(asciiArt.paper)

        print("\nComputer chose :")
        print(asciiArt.paper)

        print(asciiArt.draw)

        isPlayerWinner = False


    elif playerChoice == 2:
        print("\nYou chose:")
        print(asciiArt.scissors)

        print("\nComputer chose :")
        print(asciiArt.paper)

        isPlayerWinner = True

elif computerChoice == "scissors":

    if playerChoice == 0:
        print("\nYou chose:")
        print(asciiArt.rock)

        print("\nComputer chose :")
        print(asciiArt.scissors)

        isPlayerWinner = True

    elif playerChoice == 1:
        print("\nYou chose:")
        print(asciiArt.paper)

        print("\nComputer chose :")
        print(asciiArt.scissors)

        isPlayerWinner = False

    elif playerChoice == 2:
        print("\nYou chose:")
        print(asciiArt.scissors)

        print("\nComputer chose :")
        print(asciiArt.scissors)

        print(asciiArt.draw)

        isPlayerWinner = False

if isPlayerWinner :
    print(asciiArt.win)
else :
    print(asciiArt.lose)
