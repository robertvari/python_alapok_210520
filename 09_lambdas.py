add_numbers = lambda a, b: a+b
# print(add_numbers)

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna"]

number_list = [5, 545, 112, 5645, 34321, 2, 42]

phonebook = {
    "06202223344": {"name": "Vári Róbert", "address": "Budapest"},
    "06201116535": {"name": "Kiss Elemér", "address": "Pécs"},
    "06303458743": {"name": "Nagy Adrienn", "address": "Debrecen"},
    "06708347623": {"name": "Tóth Barna", "address": "Nyíregyháza"},
}

# print(sorted(name_list, key=lambda name: name.split()[-1]))
print(sorted(phonebook, key=lambda phone: phonebook[phone]["address"]))