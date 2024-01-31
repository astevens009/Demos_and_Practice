"""
Using examples in Real Python 
Site: https://realpython.com/intro-to-python-threading/
"""

import logging
import threading 
import time

def thread_function(name):
    logging.info("Thread %s: startinhg", name)
    time.sleep(3)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    threads = list()
    for index in range(3):
        logging.info("Main  : create and start thread %d.", index)
        print()
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()