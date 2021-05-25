from utilities import phonebook_utils as utils


def main():
    print("-"*50, "Phonebook", "-"*50,)

    utils.load_phonebook()

    menu_functions = {
        "1": utils.print_phonebook,
        "2": utils.find_contact,
        "3": utils.add_contact,
        "4": utils.edit_contact,
        "5": utils.delete_contact,
        "6": utils.close_phonebook,
    }

    user_choice = utils.menu()

    # todo refine this
    if not menu_functions.get(user_choice):
        exit()

    menu_functions[user_choice]()


if __name__ == '__main__':
    main()