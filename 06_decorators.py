import time, random
from utilities.decorators import my_timer, do_nothing


@do_nothing
@my_timer
def worker_1(max_time):
    print(f"<<< worker_1 started >>> Max time: {max_time}")
    time.sleep(random.randint(1, max_time))
    print("<<< worker_1 >>> I'm done!")

worker_1(5)