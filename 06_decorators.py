import time, random


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


@do_nothing
@my_timer
def worker_1(max_time):
    print(f"<<< worker_1 started >>> Max time: {max_time}")
    time.sleep(random.randint(1, max_time))
    print("<<< worker_1 >>> I'm done!")

worker_1(5)