import time, random, threading

download_event = threading.Event()
data_ready_event = threading.Event()


def download_worker():
    print("download_worker started")

    time.sleep(random.randint(1, 20))

    print("Download ready!")
    download_event.set()


def process_worker():
    download_event.wait()
    print("process_worker started")

    time.sleep(random.randint(1, 20))

    print("process_worker finished")
    download_event.clear()
    data_ready_event.set()


downloader_thread = threading.Thread(target=download_worker)
process_worker_thread = threading.Thread(target=process_worker)

downloader_thread.start()
process_worker_thread.start()
# print(download_event.isSet())
# download_event.set()
# print(download_event.isSet())
# download_event.clear()