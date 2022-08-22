""""Example of conditional if else statements"""

SECRET: int = 3

print("I'm thinking of a number 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly! ")
    print("Have a good day")
else:
    print("Try again")
    if guess > SECRET: 
        print("Lower")
    else: 
        print("higher")

print("Game over")