

#  real example of multiprocessing 


import time
import sys
import multiprocessing
import math

# making system limitation

sys.set_int_max_str_digits(100000)

def fact(number):
    result = math.factorial(number)
    return result



if __name__ == '__main__':
    
    numbers = [5000,6000,7000,8000]
    
    st = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(fact,numbers)
    end = time.time()
    
    
    print(f"Results : {results}")
    print(f"time execution : {end-st}")