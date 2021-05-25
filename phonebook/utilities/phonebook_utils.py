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
    print("-"*50)
    for k, v in PHONEBOOK.items():
        print(f"Name: {v}\t\t Phone: {k}")
    print("-" * 50)


def find_contact():
    _name = input("Name:")

    result = None
    for phone, name in PHONEBOOK.items():
        if _name.lower() == name.lower():
            result = f"Name: {name} Phone: {phone}"
            break

    if result:
        print(result)
    else:
        print(f"I couldn't find {_name} in the phonebook.")


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
    _name = input("Name:")
    new_phone = input("New Phone number:")

    for phone, name in PHONEBOOK.items():
        if _name.lower() == name.lower():
            del PHONEBOOK[phone]
            PHONEBOOK[new_phone] = _name
            break

    save_phonebook()


def save_phonebook():
    with open(DATA_FILE, "w") as f:
        json.dump(PHONEBOOK, f)


def delete_contact():
    _name = input("Name:")

    for phone, name in PHONEBOOK.items():
        if _name.lower() == name.lower():
            del PHONEBOOK[phone]
            break

    save_phonebook()


def close_phonebook():
    print("See you later!")
    exit()


if __name__ == '__main__':
    load_phonebook()
    print(PHONEBOOK)