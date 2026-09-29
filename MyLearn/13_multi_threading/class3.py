


### multithreading with thread pool executor 

from concurrent.futures import ThreadPoolExecutor
import time


def print_num(number):
    time.sleep(2)
    return f"Number : {number}"


numbers = [ i for i in range(1,10)]


# creating 3 threading for output 

with ThreadPoolExecutor(max_workers=3) as exe:
    results = exe.map(print_num,numbers)


# displaying the result 

for i in results:
    print(i)