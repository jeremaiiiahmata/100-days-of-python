import words
import hangman_art
import random

lives = 6 # Lives
gameOver = False # If user is winning

randomWord = random.choice(words.letters)  #Chooses a random word in the words.py file
lettersRemaining = len(randomWord)

blank = "" #Blank
for i in randomWord :
    blank += "_"

def two_space():
    print("\n\n")



print("************************-----WELCOME TO HANGMAN-----************************")
print("************************-----by Jeremaiah Mata------************************")
two_space()

while not gameOver:

    userGuess = False  # If user has guessed a correct word

    print(f"************************-----{lives}/6 LIVES LEFT-----************************")
    print(f"{blank}")
    guess = input("Guess a letter :").lower()

    index = 0 #Initializes the index

    for item in randomWord :
        if guess == item :
            blankList = list(blank)#Converts the blank string into a list
            blankList[index] = str(guess) #Locates the specific location in string to be replaced by the correct letter.
            blank = "".join(blankList) #Replaces the current value of the blank variable with the blankList array converted to String.

            userGuess = True
            index += 1
            lettersRemaining -= 1
        else :
            index += 1

    if userGuess: #Checks if the user has guess correct.
        two_space()
        print("You are correct!")
    else :
        two_space()
        print("You are wrong!")
        lives -= 1

    print(hangman_art.hangmanAscii[lives])


    if lives == 0 :
        gameOver = True
        print(hangman_art.lose)

    if lettersRemaining == 0:
        gameOver = True
        print(hangman_art.win)


two_space()
print("*******************GAME OVER!*******************")






