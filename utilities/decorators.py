import time


def my_timer(func):
    print("my_timer started.")

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f"<<<Process Timer>>> {time.time() - start_time}")

    return wrapper


def do_nothing(func):
    print("do_nothing started.")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper