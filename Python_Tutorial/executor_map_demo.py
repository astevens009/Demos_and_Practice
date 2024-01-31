from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'Starting the task (thread) {id}...')
    sleep(3)
    return f'Done with task (thread) {id}'

def task_run1():
    start = perf_counter()

    with ThreadPoolExecutor() as executor:
        results = executor.map(task, [1, 2])

        for result in results:
            print(result)

        # print("Value of reults:")
        # for r in results:
        #     print(r)

    finish = perf_counter()

    print(f"It took {finish-start} second(s) to finish")

if __name__ == '__main__':
    task_run1()