import random

MAX_TRIES = 3
MIN_NUMBER = 0
MAX_NUMBER = 10
PLAYER_CREDITS = 0
DEBUG = True


def intro():
    print("-"*50, "MAGIC NUMBER", "-"*50,)
    print(f"I guessed a number between {MIN_NUMBER}-{MAX_NUMBER}")
    print(f"You have {MAX_TRIES} tries to guess my number.")


def game():
    global MAX_TRIES
    global PLAYER_CREDITS

    magic_number = get_magic_number()
    if DEBUG:
        print(f"<<<The number is>>> {magic_number}")

    player_guess = get_player_number()

    while not magic_number == player_guess:
        set_max_tries(-1)
        if MAX_TRIES == 0:
            break

        print("Wrong guess.")
        print(f"You have {MAX_TRIES} tries left.")
        player_guess = get_player_number()

    if player_guess == magic_number:
        print(f"You win! My number was {magic_number}")
        print("You win 1 credit")
        set_player_credits(1)


def get_magic_number() -> str:
    return str(random.randint(MIN_NUMBER, MAX_NUMBER))


def get_player_number():
    return input("Your guess?")


def set_max_tries(value):
    global MAX_TRIES
    MAX_TRIES += value


def set_player_credits(value):
    global PLAYER_CREDITS
    PLAYER_CREDITS += value


def get_player_credits():
    return PLAYER_CREDITS


if __name__ == '__main__':
    intro()