"""
Using examples in: https://pythonspot.com/threading/
"""

import threading

# Defining our thread class
class MyThread(threading.Thread):
    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        print(str(self.__x))

# Initiating 10 threads
for x in range(10):
    print("Process {}: ".format(x + 1), end=" ")
    MyThread(x).start()
    print()