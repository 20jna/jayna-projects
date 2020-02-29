#Noah's nice ol' hangman game
#Noah Choi and Jay Na
#Worked a lil with William Pangburn

def main():
#Initial Set up
    import sys
    lives = 6
    player1 = str(input("Player 1 Please Enter a Word or Phrase. (Player 2 Look Away!): "))
#If the Player Enters a Number in their initial phrase
    if "1" in player1 or "2"in player1 or "3" in player1 or "4" in player1 or "5" in player1 or "6" in player1 or " 7 " in player1 or "8" in player1 or "9" in player1 or "0" in player1:
        print("Please Do Not Use Numbers in Your Phrase.  Try Again.")
        player1 = str(input("Player 1 Please Enter a Word or Phrase. (Player 2 Look Away!): "))
#If the Player Doesn't Follow The Directions They Will Be Made Fun Of
        if "1" in player1 or "2"in player1 or "3" in player1 or "4" in player1 or "5" in player1 or "6" in player1 or " 7 " in player1 or "8" in player1 or "9" in player1 or "0" in player1:
            input("You Obviously Cannot Follow Directions.  Come Back After You Graduate Kindergarten.  Game Will Now Close: ")
            sys.exit()
#If the Player Follows Directions
        else:
            print("Player 1 Has Entered a Word or Phrase.  Game will now start.")
            guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))
            blanks = "_"
            multiplyer = int(len(player1))
            blankstring = blanks*multiplyer
            UserGuesses = ""
#The Player enters a successful string the first time around
    else:
        print("Player 1 Has Entered a Word or Phrase.  Game will now start.")
        guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))
        blanks = "_"
        multiplyer = int(len(player1))
        blankstring = blanks*multiplyer
        UserGuesses = ""
        testblank = ""
        CorrectGuesses = ""



# Game Start
    while guess:
#The Guess is in the Phrase
        while guess in player1.upper() or guess in player1.lower():
#The Guess has already been stated
            if guess in str(UserGuesses):
                print("You Have Already Entered That Letter.  Try Another.")
                guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))
#The Guess is correct
            else:
                print("Correct.  Good Guess")
                CorrectGuesses = CorrectGuesses + guess
                UserGuesses = UserGuesses + guess
                print("Your Guesses:","", UserGuesses)
                print("Number of Lives Remaining:", lives)
                #Code for the spaces and the loop that governs it
                for c in player1:
                    if c in guess:
                        testblank = testblank + guess
                    elif c in CorrectGuesses.upper() or c in CorrectGuesses.lower():
                        testblank = testblank + c
                    elif c in ",-'' ":
                        testblank = testblank + c
                    elif c in guess.upper() or c in guess.lower():
                        testblank = testblank + c
                    else:
                        testblank = testblank + "_"
                print(testblank)
#The Player has won the game
                if testblank == player1:
                    input("Congratulations.  You Have Won the Game! Press Any Button to Close: ")
                    sys.exit()
                else:
                    testblank = ""
                    guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))

#The Guess is Incorrect
        while guess not in player1:
#The Guess is not a letter; No Lives are lost
            if guess in "1234567890,<.>/?-_=+;:)(*&^%$#@!~``)":
                UserGuesses = UserGuesses + guess
                print("Your Guesses:","", UserGuesses)
                print("The Character You Have Entered in Not Valid.  Please Only Enter Letters.")
                guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))
#Game Over Criteria
            elif lives == 0:
                    print("You Have Run Out of Lives and Are Now Dead.  Game Over.")
                    input(": ")
                    close()
#The Guess is an incorrect letter.  One life is lost.
            else:
                lives = lives - 1
                print("That Letter is Not in The Word/Phrase.  One Life Has Been Lost.")
                UserGuesses = UserGuesses + guess
                print("Your Guesses:","", UserGuesses)
                #Code for the spaces and the loop that governs it
                for c in player1:
                    if c in guess:
                        testblank = testblank + guess
                    elif c in CorrectGuesses.upper() or c in CorrectGuesses.lower():
                        testblank = testblank + c
                    elif c in ",-'' ":
                        testblank = testblank + c
                    elif c in guess.upper() or c in guess.lower():
                        testblank = testblank + c
                    else:
                        testblank = testblank + "_"
                print(testblank)
#The Player has won the game
                if testblank == player1:
                    input("Congratulations.  You Have Won the Game! Press Any Button to Close: ")
                    sys.exit()
                else:
                    testblank = ""
                    print("Number of Lives Remaining:", lives)
                    guess = str(input("Player Two. Please Guess a Letter. (No Numbers): "))

main()