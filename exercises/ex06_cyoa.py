""""Choose your own adventure project."""
__author__ = "730554383"

from random import randint
PLAYER_NAME: str = input("Enter your name. ")
ENEMY_NAME: str = input("Enter a creature you would like to fight. ")
points: int = 5
enemy_points: int = 5
ENEMY_ATTACK_OPTIONS: list[str] = ["kick", "tackle", "punch"]


def greet() -> None:
    """Greeting to the player and a introduction to the game."""   
    print(f"Welcome {PLAYER_NAME}, today you will be battling a {ENEMY_NAME}")
    print(f"You currently have {points} points and the {ENEMY_NAME} has {enemy_points} points")
    print("You have three options to attack: punch, kick, and tackle. Punch beats kick, tackle beats punch, and kick beats tackle.")
    print("You can also run away, but you forfeit the match and end the game.")
    print(f"The goal is to outlast the {ENEMY_NAME} and win the game, good luck.")


def kick() -> None:
    """Option when user chooses kick."""
    global enemy_points
    global points
    print(f"{PLAYER_NAME} has chosen to kick.")
    i: int = randint(1, 2)
    attack: str = ENEMY_ATTACK_OPTIONS[i]
    if attack == "tackle":
        print(f"{PLAYER_NAME} lands a blow and hurts the {ENEMY_NAME}")
        enemy_points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points}, {ENEMY_NAME} = {enemy_points}")
    else:
        print(f"{ENEMY_NAME} lands a blow and hurts {PLAYER_NAME}")
        points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points}, {ENEMY_NAME} = {enemy_points}")


def main() -> None:
    greet()
    print(PLAYER_NAME)
    global points
    global enemy_points
    while points > 0 or enemy_points > 0:
        attack_choice: str = input("Choose an attack (kick, tackle, or punch), or run away: ")
        print(attack_choice)
        if attack_choice == "kick":
            kick()
        #elif attack_choice == "punch":
            #punch()
        #elif attack_choice == "tackle":
            #tackle()
        else:
            attack_choice = input("Not a valid choice please try again: ")


if __name__ == "__main__":
    main()