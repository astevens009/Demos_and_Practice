"""
Using examples in Real Python 
Site: https://realpython.com/intro-to-python-threading/
"""

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    print("You've just started the thread...\n")
    time.sleep(2)
    print("The thread is now done.\n")
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main      : before creating thread")

    # NOTE: Setting the daemon thread
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info("\nMain      : before running thread")
    x.start()

    logging.info("Main      : wait for the thread to finish")
    #x.join()

    logging.info("Main      : complete")
    print()
