import time, random, threading


def worker_1(max_time):
    print(f"<<< worker_1 started on {threading.currentThread().name}>>> Max time: {max_time}")
    time.sleep(random.randint(1, max_time))
    print("<<< worker_1 >>> I'm done!")


def worker_2(max_time):
    print(f"<<< worker_2 started {threading.currentThread().name}>>> Max time: {max_time}")
    time.sleep(random.randint(1, max_time))
    print("<<< worker_2 >>> I'm done!")


def worker_3(max_time):
    print(f"<<< worker_3 started {threading.currentThread().name}>>> Max time: {max_time}")
    time.sleep(random.randint(1, max_time))
    print("<<< worker_3 >>> I'm done!")


t1 = threading.Thread(target=worker_1, args=[4])
t2 = threading.Thread(target=worker_2, args=[10])
t3 = threading.Thread(target=worker_3, args=[20])

t1.start()
t2.start()
t3.start()

print(f"All process finished {threading.currentThread().name}")