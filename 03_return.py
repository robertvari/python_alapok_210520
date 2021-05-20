def add_numbers(a: int, b: int) -> int:
    return a+b


def multiply_numbers(a: int, b: int) -> int:
    return a*b


def do_nothing():
    pass

add_result = add_numbers(2, 10)
multiply_result = multiply_numbers(add_result, 10)

print(do_nothing())