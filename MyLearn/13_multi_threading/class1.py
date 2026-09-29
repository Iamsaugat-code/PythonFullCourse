
#### Threading in Python:
#### Threading is a way to run multiple tasks concurrently within the same program.

#### Why is it used?
#### It is used to make programs more responsive, especially when tasks are waiting for things like files, network requests, or user input.

#### Example: Downloading multiple files at the same time



import threading
import time

def numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers : {i}")


def words():
    for word in "ABCDE":
        time.sleep(2)
        print(f"Alphate : {word}")


def syntax():
    for s in '#%$^%*':
        time.sleep(2)
        print(f"Syntax : {s}")

# now creating thread

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=words)
t3 = threading.Thread(target=syntax)
start = time.time()

# starting threading
t1.start()
t2.start()
t3.start()


# waiting for thread to complete
t1.join()
t2.join()
t3.join()

end = time.time()-start
print(end)



# note -- t1 = threading.Thread(target=funcname)