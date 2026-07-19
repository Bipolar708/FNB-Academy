#A simple guessing game

secret_word="python"


while True:
    guess=input("Guess the programming language we are using: ").lower()

    if guess==secret_word:
        print("You have guessed the correct language !!!")
        break
    else:
        print("Incorrect guess, Try again !!!")

