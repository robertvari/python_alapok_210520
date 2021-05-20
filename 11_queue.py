import random, time, threading, queue
from utilities.file_utils import get_all_files

job_list = queue.Queue()

folder_path = r"C:\Work\_PythonSuli\python_alapozo\alapok_02"
[job_list.put(i) for i in get_all_files(folder_path)]


def worker():
    print(f"<<< worker_1 started on {threading.currentThread().name}>>>")
    time.sleep(random.randint(1, 20))
    print("<<< worker_1 >>> I'm done!")
