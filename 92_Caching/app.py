import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(8))
print('done for 8')
print(fx(4))
print('done for 4')
print(fx(6))
print('done for 6')
print(fx(2))
print('done for 2')
print(fx(8))
print('done for 8')
print(fx(4))
print('done for 4')
print(fx(6))
print('done for 6')
print(fx(2))
print('done for 2')