import random
import art
import game_data

NAME = "name"
COUNT = "follower_count"
DESC = "description"
COUNTRY = "country"

def generateData():
    index = random.randint(0, len(game_data.data)-1)

    return game_data.data[index]

def compareCount(a, b):
    if a[COUNT] > b[COUNT]:
        return "a"
    else :
        return "b"

def checkAnswer(winner, ans):
    if ans.lower() == winner:
        return True
    else :
        return False

def createSpace():
    print("\n" * 20)

def checkForDuplicate(a, b):
    if a == b:
        return True
    else :
        return False

gameOver = False
score = 0

print(art.logo)

optionA = generateData()
optionB = generateData()

while not gameOver:

    isDuplicate = checkForDuplicate(optionA, optionB)

    while isDuplicate:

        print("Changing Option B...")
        optionB = generateData()

        if checkForDuplicate(optionA, optionB):
            isDuplicate = True
        else:
            isDuplicate = False

    print(f"A : {optionA[NAME]}, a {optionA[DESC]} from {optionA[COUNTRY]}.")
    print("------VS------")
    print(f"B : {optionB[NAME]}, a {optionB[DESC]} from {optionB[COUNTRY]}.")

    winner = compareCount(optionA, optionB)

    choice = input("Choose an option : ")

    result = checkAnswer(winner, choice)

    if result :
        optionA = optionB
        optionB = generateData()
        score += 1

        print("Correct! 😊")
        createSpace()
    else :
        gameOver = True

print("Game over. Thank you for playing!")
print(f"Your score is {score}")