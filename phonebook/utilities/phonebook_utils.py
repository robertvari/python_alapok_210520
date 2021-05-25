import json, os

PHONEBOOK = {}
DATA_FILE = "phonebook_data.json"


def menu() -> str:
    print(
        "1. Print Phonebook\n"
        "2. Find Contact\n"
        "3. Add Contact\n"
        "4. Edit Contact\n"
        "5. Delete Contact\n"
        "6. Exit"
    )

    return input()


def print_phonebook():
    print("print_phonebook")


def find_contact():
    print("find_contact")


def load_phonebook():
    global PHONEBOOK

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            PHONEBOOK = json.load(f)

def add_contact():
    phone = input("Phone:")
    name = input("Name:")

    PHONEBOOK[phone] = name

    save_phonebook()
    print(f"New contact added: Phone: {phone} Name: {name}")


def edit_contact():
    print("edit_phonebook")


def save_phonebook():
    with open(DATA_FILE, "w") as f:
        json.dump(PHONEBOOK, f)


def delete_contact():
    print("save_phonebook")


def close_phonebook():
    print("See you later!")
    exit()


if __name__ == '__main__':
    load_phonebook()
    print(PHONEBOOK)