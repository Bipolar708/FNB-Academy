#Build an interactive program that continuously asks an arcade player for their game score.
#1. Start an intentional infinite loop using while True:.
#2. Inside the loop, ask the user to enter a game score next to the flashing cursor.
#3. If they type the word “stop” (clean it up with .strip().lower()), print “Game session ended!” and use a break statement to shut down the loop.
#4. Otherwise, cast their input into an int, check if the score is greater than 100, and print either “Wow! That’s a new high score!” or “Good try, keep playing!” based on the value.

while True:
    #inputs
    current_score=input("Enter your current score: ")

    if current_score.strip().lower()=="stop":
        print("Game session ended")
        break
    elif int(current_score)>100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")