my_number = 10
my_list = ["Robert", "Tamás", "Csaba"]
my_list2 = ("Robert", "Tamás", "Csaba")


def set_number(number):
    print(id(number))
    number += 100
    return number


# my_number = set_number(my_number)
# print(id(my_number))
# print(my_number)

def edit_list(my_list):
    print(id(my_list))
    my_list[0] = "Edited"
    print(id(my_list))


edit_list(my_list)
print(my_list)