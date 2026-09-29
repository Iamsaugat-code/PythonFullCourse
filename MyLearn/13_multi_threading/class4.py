


# ### multiprocessing with thread pool executor 

from concurrent.futures import ThreadPoolExecutor
import time


def square(num):
    time.sleep(2)
    return f"Sqaure : {num*num}"

data = [i for i in range(1,10)]

# creating three process with threadpool executor


if __name__ =='__main__':

    with ThreadPoolExecutor(max_workers=3) as ex:
        results = ex.map(square,data)
       
    st = time.time()
    for i in results:
        print(i)
    end = time.time() - st
    print(end)
    
# Run the code inside this block only when this file is run directly if __name__ =='__main__':