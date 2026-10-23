# Config
START_HEARTS = 6
HEART = "♥"
SKETCH_BASE = r"""
      O
     /|\
     / \
"""
UNKNOWN_FILLER = "_"

# State
game_running = True
correctWord: str
hearts = START_HEARTS
currentGuess: list = []

def game_present():
    hstr = (hearts*HEART).replace(""," ")
    print(f"{hstr}{SKETCH_BASE}\n{str().join(currentGuess)}")

def game_end():
    game_present()
    print("Game over")
    print(f"Rätt ord var: {correctWord}")   

def game_guess() -> bool:
    global hearts, currentGuess
    # Only allow guesses on a single character
    guess = input("Gissa: ").lower().strip()[0]
    correct = False

    # For every character in guess.
    for i in range(len(guess)):
        cGuess = guess[i]
        # Check if character exists in correct word
        for i2 in range(len(correctWord)):
            cWord = correctWord[i2]
            if cGuess == cWord:
                correct = True
                currentGuess[i2] = cGuess

    if correct == False:
        hearts -= 1
        print("Fel svar.")
    game_present()

def game_hasWon() -> bool:
    return correctWord == "".join(currentGuess)

def main():
    global correctWord, game_running, hearts, currentGuess
    correctWord = input("Ord att gissa på: ").lower()
    currentGuess = list(UNKNOWN_FILLER * len(correctWord))

    # Game loop
    while game_running:
        game_guess()
        print()
        if hearts == 0:
            game_running = False
            break

        if game_hasWon():
            print("-------------")
            print("Du vann!")
            break

    game_end()

if __name__ == "__main__":
    main()