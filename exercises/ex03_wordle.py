"""Wordle!!!"""
__author__ = "730554383"


def contains_char(large: str, chr: str) -> bool:
    """Searches to see if a word contains a certain character!"""
    assert len(chr) == 1
    i: int = 0
    present: bool = False

    while i < len(large) and not present:
        if chr == large[i]:
            present = True
        else:
            i += 1
    return present


def emojified(guess: str, secret: str) -> str:
    """Returns an string of emojis based on the guess!"""
    assert len(secret) == len(guess)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emojis: str = ""
    v: int = 0
    while v < len(guess):
        if contains_char(secret, guess[v]) and secret[v] == guess[v]:
            emojis += green_box
            v += 1
        elif contains_char(secret, guess[v]):
            emojis += yellow_box
            v += 1
        else:
            emojis += white_box
            v += 1
    return emojis


def input_guess(length: int) -> str:
    """Creates a guess of desired length."""
    user_guess: str = input(f"Enter a {length} character word: ")
    while len(user_guess) != length:
        user_guess = input(f"That wasn't {length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    chance: int = 1
    ifwon: bool = False
    secret_word: str = "codes"
    while chance < 7 and not ifwon:
        print(f"=== Turn {chance}/6 ===")
        person_guess: str = input_guess(len(secret_word))
        print(emojified(person_guess, secret_word))
        if person_guess == secret_word:
            print(f"You won in {chance}/6 turns!")
            ifwon = True
        else: 
            chance += 1
    if chance == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
