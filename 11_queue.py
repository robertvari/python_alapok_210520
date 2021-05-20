import random, time, threading, queue
from utilities.file_utils import get_all_files

job_list = queue.Queue()

folder_path = r"C:\Work\_PythonSuli\python_alapozo\alapok_02"
[job_list.put(i) for i in get_all_files(folder_path)]


def worker():
    while not job_list.empty():
        file_path = job_list.get()

        print(f"<<< {threading.currentThread().name} working on>>> file path: {file_path}")
        time.sleep(random.randint(1, 20))
        print(f"<<< {threading.currentThread().name} >>> process done!")

        job_list.task_done()

    print(f"<<< {threading.currentThread().name} >>> finished all tasks.")


for _ in range(16):
    t = threading.Thread(target=worker)
    t.start()

