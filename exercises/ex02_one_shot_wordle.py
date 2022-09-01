"""One shot wordle"""
__author__ = "730554383"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emoji: str = ""

while len(guess) != len(secret):
   guess = input("That was not 6 letters! Try again: ") 

while i < len(secret):  
    v: int = 0
    present: bool = False
    while present == False and v < len(secret):
        if guess[i] == secret[v]:
            present = True
        else:
            v += 1
    if guess[i] == secret[i] and present == True:
        emoji += GREEN_BOX
        i+=1
    elif present == True:
        emoji += YELLOW_BOX
        i+=1
    else:
        emoji += WHITE_BOX
        i+=1


print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
