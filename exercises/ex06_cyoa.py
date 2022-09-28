""""Choose your own adventure project."""
__author__ = "730554383"

from random import randint
player: str = ""
enemy: str = ""
points: int = 5
enemy_points: int = 5
ENEMY_ATTACK_OPTIONS: list[str] = ["kick", "tackle", "punch"]


def greet() -> None:
    """Greeting to the player and a introduction to the game."""
    global player
    global enemy
    player = input("Enter your name: ")   
    enemy = input("Enter a creature you would like to fight: ")
    print(f"Welcome {player}, today you will be battling a {enemy}")
    print(f"You currently have {points} points and the {enemy} has {enemy_points} points")
    print("You have three options to attack: punch, kick, and tackle. Punch beats kick, tackle beats punch, and kick beats tackle.")
    print("You can also run away, but you lose the fight and end the game.")
    print(f"The goal is to outlast the {enemy} and win the game, good luck.")


def kick() -> None:
    """Option when user chooses kick."""
    global enemy_points
    global points
    print(f"{player} has chosen to kick.")
    i: int = randint(1, 2)
    attack: str = ENEMY_ATTACK_OPTIONS[i]
    if attack == "tackle":
        print(f"{player} kicks the {enemy} hurting it.")
        enemy_points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")
    else:
        print(f"{enemy} attacks {player} with a {attack} and hurts {player}")
        points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")


def punch() -> None:
    """Option when user chooses punch."""
    global enemy_points
    global points
    print(f"{player} has chosen to punch.")
    i: int = randint(0, 1)
    attack: str = ENEMY_ATTACK_OPTIONS[i]
    if attack == "kick":
        print(f"{player} punches the {enemy} hurting it")
        enemy_points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")
    else:
        print(f"{enemy} attacks {player} with a {attack} and hurts {player}")
        points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")


def tackle() -> None:
    """Option when user chooses tackle."""
    global enemy_points
    global points
    print(f"{player} has chosen to tackle.")
    options: list[int] = [0, 2]
    i: int = randint(0, 1)
    attack: str = ENEMY_ATTACK_OPTIONS[options[i]]
    if attack == "punch":
        print(f"{player} tackles the {enemy} hurting it")
        enemy_points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")
    else:
        print(f"{enemy} attacks {player} with a {attack} and hurts {player}")
        points -= 1
        print(f"Current scores: {player} = {points} || {enemy} = {enemy_points}")


def run_away() -> None:
    """Options when user wants to quit. """
    global points
    print(f"{player} has chosen to run away with {points} points.")
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
        print(f"{player} lost the fight")
        quit()
    else: 
        print(f"{player} has won the fight with {points} points left, congrats. ")
        quit()
    


if __name__ == "__main__":
    main()