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
        print(f"{PLAYER_NAME} kicks the {ENEMY_NAME} hurting it")
        enemy_points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")
    else:
        print(f"{ENEMY_NAME} attacks {PLAYER_NAME} with a {attack} and lands a blow")
        points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")


def punch() -> None:
    """Option when user chooses punch."""
    global enemy_points
    global points
    print(f"{PLAYER_NAME} has chosen to punch.")
    i: int = randint(0, 1)
    attack: str = ENEMY_ATTACK_OPTIONS[i]
    if attack == "kick":
        print(f"{PLAYER_NAME} punches the {ENEMY_NAME} hurting it")
        enemy_points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")
    else:
        print(f"{ENEMY_NAME} attacks {PLAYER_NAME} with a {attack} and lands a blow")
        points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")


def tackle() -> None:
    """Option when user chooses tackle."""
    global enemy_points
    global points
    print(f"{PLAYER_NAME} has chosen to tackle.")
    options: list[int] = [0, 2]
    i: int = randint(0, 1)
    attack: str = ENEMY_ATTACK_OPTIONS[options[i]]
    if attack == "punch":
        print(f"{PLAYER_NAME} tackles the {ENEMY_NAME} hurting it")
        enemy_points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")
    else:
        print(f"{ENEMY_NAME} attacks {PLAYER_NAME} with a {attack} and lands a blow")
        points -= 1
        print(f"Current scores: {PLAYER_NAME} = {points} || {ENEMY_NAME} = {enemy_points}")


def run_away() -> None:
    """Options when user wants to quit. """
    global points
    print(f"{PLAYER_NAME} has chosen to run away and there for loses the game")
    points = 0



def main() -> None:
    greet()
    global points
    global enemy_points
    while points > 0 and enemy_points > 0:
        attack_choice: str = input("Choose an attack (kick, tackle, or punch), or run away: ")
        if attack_choice == "kick":
            kick()
        elif attack_choice == "punch":
            punch()
        elif attack_choice == "tackle":
            tackle()
        elif attack_choice == "run away":
            run_away()
        else:
            attack_choice = input("Not a valid answer, please enter another choice: ")
    if points == 0:
        print("You have lost the fight")
        quit()
    else: 
        print(f"{PLAYER_NAME} has won the fight with {points} points left, congrats. ")
        quit()
    


if __name__ == "__main__":
    main()