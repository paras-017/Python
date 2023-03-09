# Local and Global variables  
'''
'''
x = 9
print(x)
def myFunc(): 
    global x
    x = 90
    y=10
    print(y)
myFunc()
print(x)
