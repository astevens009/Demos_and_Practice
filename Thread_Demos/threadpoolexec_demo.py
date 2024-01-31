from concurrent.futures import ThreadPoolExecutor
import time
import random

def multiply_by_2(value):

    print(f"Multiplying {value} by 2...")
    time.sleep(2)
    return value * 2



def run_multiply_by_2(num_list):

    start = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        products = executor.map(multiply_by_2, num_list)

        print("Values:")
        for value in products:
            print(value)

    finish = time.perf_counter()

    print(f"It took {finish-start} second(s) to finish.")


if __name__ == '__main__':

    numbers = []
    for _ in range(5):
        numbers.append(random.randint(1, 10))

    run_multiply_by_2(numbers)