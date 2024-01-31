from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'Staring the thread {id}...')
    sleep(2)
    return f'Done with thread {id}'

def task_run_1():
    print("Starting first demo...\n")
    start = perf_counter()

    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(task, 1)
        f2 = executor.submit(task, 2)

        print(f"Result: {f1.result()}")
        print(f"Result: {f2.result()}")

    finish = perf_counter()

    print(f"It took {finish-start} second(s) to finish")

def task_run_2():
    print("Staring second demo...\n")
    start = perf_counter()

    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(task, 1)
        print(f"Result: {f1.result()}")
        
        f2 = executor.submit(task, 2)
        print(f"Result: {f2.result()}")


    finish = perf_counter()

    print(f"It took {finish-start} second(s) to finish")


if __name__ == '__main__':
    task_run_1()
    # task_run_2()