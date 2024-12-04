import random
import asciiArt

RANDOM_NUMBER = random.randint(1, 101)

def setLives(difficulty, livesRemaining):
    if difficulty.lower() == "easy":
        livesRemaining = 10
        return livesRemaining
    elif difficulty.lower() == "hard":
        livesRemaining = 5
        return livesRemaining
    else:
        print("Wrong input. Try again.")

def setDifficulty(lives):
    difficulty = input("Choose a difficulty ['easy' or 'hard'] : ")
    lives = setLives(difficulty, lives)

    return lives

def checkAnswer(guess):
    if guess > RANDOM_NUMBER:
        print("\nToo high! 👆")
        return False
    elif guess < RANDOM_NUMBER:
        print("\n Too Low! 👇")
        return False
    else:
        print("\nYou've guessed it correctly! 😎")
        print(f"The number is : w[{RANDOM_NUMBER}]")
        return True



def game():
    lives = 0
    gameOver = False

    print(asciiArt.intro)
    print(RANDOM_NUMBER)
    lives = setDifficulty(lives)

    while not gameOver :
        if lives > 0 :
            print(f"\n--*** You have {lives} left ***--")
            guess = int(input("Guess a number : "))
            hasGuessed = checkAnswer(guess)

            if hasGuessed:
                gameOver = True
            else :
                lives -= 1
        else :
            gameOver = True
            print("\nYou lost. Try again.😟")
            print(f"The correct answer is {RANDOM_NUMBER}")

    print(f"\n\n{asciiArt.gameOver}")

game()