

# Multiprocessing in Python:
# Multiprocessing is a way to run multiple processes at the same time.

# Why is it used?
# It is mainly used for CPU-intensive tasks to improve performance by using multiple CPU cores.

# Example: Processing large datasets or performing heavy calculations simultaneously.



import multiprocessing
import time


def square():
    for i in range(5):
        time.sleep(2)
        print(f"square : {i*i}")

def cube():
    for i in range(5):
        time.sleep(2)
        print(f"cube : {i*i*i}")
        

p1 = multiprocessing.Process(target=square)
p2 = multiprocessing.Process(target=cube)



if __name__ == '__main__':
    st = time.time()
    # started process 
    p1.start()
    p2.start()
    
    # wait for complete
    
    p1.join()
    p2.join()
    
    end = time.time() - st
    print(end)


        