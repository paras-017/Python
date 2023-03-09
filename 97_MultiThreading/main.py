import threading
import time

def myFunc(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

#Normal Code
time1 = time.perf_counter()
myFunc(4)
myFunc(2)
myFunc(1)
time2 = time.perf_counter()
print(time2-time1)

#Threading Code
time3 = time.perf_counter()
t1 = threading.Thread(target=myFunc, args=[4])
t2 = threading.Thread(target=myFunc, args=[2])
t3 = threading.Thread(target=myFunc, args=[1])
time4 = time.perf_counter()
print(time4-time3)


# t1.start()
# t2.start()
# t3.start()
