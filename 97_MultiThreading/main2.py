import threading
import time
from concurrent.futures import ThreadPoolExecutor

def myFunc(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def poolingDemo():
    with ThreadPoolExecutor() as executor: 
        # future1 = executor.submit(myFunc,3)
        # future2 = executor.submit(myFunc, 15)
        # future3 = executor.submit(myFunc,2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())


        l = [3,5,1,2]
        results = executor.map(myFunc,l)
        for result in results:
            print(result)
        
poolingDemo()