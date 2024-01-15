import threading
import schedule
import time
import atexit

import config


def my_function():
    import database
    config.run()

def start_thread_safely():
    if threading.main_thread().is_alive():
        threading.main_thread().join()

    thread = threading.Thread(target=my_function)
    thread.start()

atexit.register(start_thread_safely)