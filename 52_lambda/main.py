# normal function but they are in smaller size and for little task
def sum(a,b):
    return a+b
print(sum(5,11))

#same sum function in lambda 
mySum  = lambda a,b:a+b
print(mySum(1000,3245))



def add(num, sq):
    return num + sq(num)

# print(add(20, lambda x: x*x))