import time, random


def my_timer(func):
    print("my_timer started.")

    def wrapper():
        start_time = time.time()
        func()
        print(f"<<<Process Timer>>> {time.time() - start_time}")

    return wrapper


@my_timer
def worker_1():
    time.sleep(random.randint(1, 10))
    print("<<< worker_1 >>> I'm done!")

@my_timer
def worker_2():
    time.sleep(random.randint(1, 10))
    print("<<< worker_2 >>> I'm done!")

@my_timer
def worker_3():
    time.sleep(random.randint(1, 10))
    print("<<< worker_3 >>> I'm done!")

worker_1()
worker_2()
worker_3()