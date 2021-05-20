def greeting(name):
    print(f"Hello {name}")


# greeting("Robert")

def greeting_2(name: str, age: int, address: str):
    print(f"Hello {name}. You are {age} old. You are from {address}")

# greeting_2("Robert", 32, "Budapest")


def greeting_3(name, age, address="Budapest"):
    print(f"Hello {name}. You are {age} old. You are from {address}")

# greeting_3("Robert", 32, "Debrecen")
# greeting_3(address="Debrecen", name="Robert", age=32)


def greeting_4(*args):
    for i in args:
        print(i)

# greeting_4(32, "Robert", "testpas123", 3.14)

def greeting_5(**kwargs):
    print(kwargs, type(kwargs))

# greeting_5(age=32, name="Robert", password="testpas123", pi=3.14)


def greeting_6(*args, **kwargs):
    print(args, kwargs)

greeting_6(1, 2, 3, 4, age=32, name="Robert", password="testpas123", pi=3.14)