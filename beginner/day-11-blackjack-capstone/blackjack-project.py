import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def drawCard() :
    """Returns a random card from the cards list."""
    return random.choice(cards)

def calculateScore(cardList) :

    if sum(cardList) == 21 and len(cardList) == 2 :
        return 0

    if 11 in cardList and sum(cardList) > 21 :
        cardList.remove(11)
        cardList.append(1)

    return sum(cardList)

def compareScore(user, comp) :
    if user == 0 and comp == 0:
        return "Draw 😁"
    elif user == 0 and comp != 0 :
        return "You win with a Blackjack! 🃏"
    elif user != 0 and comp == 0:
        return "You lose, Computer has Blackjack! 🃏"
    elif user > 21 :
        return "You lose! You went over. 😔"
    elif comp > 21 :
        return "You win! Computer went over. 😁"
    elif user > comp:
        return "You win! 😁"
    else :
        return "You lose! 😔"

def playGame():

    userCards = []
    computerCards = []
    isGameOver = False
    computerScore = -1
    userScore = -1

    for i in range(2):
        userCards.append(drawCard())
        computerCards.append(drawCard())

    while not isGameOver :
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)

        print("\n")
        print(f"User : {userCards} Score = {userScore}")
        print(f"Computer : {computerCards[0]}")


        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else :
            print("\n")
            drawAnother = input("Do you want to draw another card? Type 'yes' or 'no' :")
            if drawAnother.lower() == 'yes' :
                userCards.append(drawCard())
            else :
                isGameOver = True

    while computerScore != 0 and computerScore < 17 :
        computerCards.append(drawCard())
        computerScore = calculateScore(computerCards)

    result = compareScore(userScore, computerScore)
    print("\n")
    print(f"{userCards} : {userScore}")
    print(f"{computerCards} : {computerScore}")
    print(result)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower() == "y" :
    print("\n" * 20)
    playGame()



