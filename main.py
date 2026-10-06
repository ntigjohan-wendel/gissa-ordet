# Config
START_HEARTS = 6
HEART = "♥"
SKETCH_BASE = r"""
      O
     /|\
     / \
"""

# State
game_running = True
guesses = []
correctWord : str
hearts = START_HEARTS
display : str

def game_present():
    hstr = (hearts*HEART).replace(""," ")
    print(f"{hstr}{SKETCH_BASE}\n{display}")

def game_end():
    game_present()
    print("Game over")
    print(f"Rätt ord var: {correctWord}")

def game_updateDisplay():
    for 
    pass

def game_guess():
    global hearts
    guess = input("Gissa: ").lower()
    guesses.append(guess)
    for i in range(len(guess)):
        if guess[i] == correctWord[i]:
            continue
        hearts -= 1
    game_present()

def main():
    global correctWord, game_running, hearts, display
    correctWord = input("Ord att gissa på: ").lower()
    display = "_"*len(correctWord)

    # Game loop
    while game_running:
        game_guess()
        if hearts == 0:
            game_running = False
            break

    game_end()

if __name__ == "__main__":
    main()