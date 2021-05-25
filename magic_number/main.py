from utilities.magic_number_utils import intro, game, get_player_credits


def main():
    intro()

    game()

    player_credits = get_player_credits()
    if player_credits == 0:
        print("You lost all your credits.\nMaybe next time")
    else:
        print(f"You have {player_credits} credits")
        user_choice = input("Do you want to try again? (y/n)")

        if user_choice == "y":
            game()
        else:
            print("Maybe next time. Bye!")
            exit()


if __name__ == '__main__':
    main()