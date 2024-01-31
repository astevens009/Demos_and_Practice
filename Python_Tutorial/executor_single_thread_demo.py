from time import sleep, perf_counter

def task(id):
    """
    Using a single thread 
    """
    print(f'Starting the task {id}...')
    sleep(2)
    return f'Done with task {id}'

if __name__ == '__main__':
    start = perf_counter()

    print(task(1))
    print(task(2))

    finish = perf_counter()

    print(f"It took {finish-start} second(s) to finish")