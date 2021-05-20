def main_func(name):
    print(f"This is main_func. Hello {name}")

    def inner_func():
        print(f"This is inner_func. Hello {name}")

    inner_func()

main_func("Robert")