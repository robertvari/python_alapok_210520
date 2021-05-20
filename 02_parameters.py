def greeting(name):
    print(f"Hello {name}")


# greeting("Robert")

def greeting_2(name: str, age: int, address: str):
    print(f"Hello {name}. You are {age} old. You are from {address}")

# greeting_2("Robert", 32, "Budapest")


def greeting_3(name, age, address="Budapest"):
    print(f"Hello {name}. You are {age} old. You are from {address}")

# greeting_3("Robert", 32, "Debrecen")
greeting_3(address="Debrecen", name="Robert", age=32)