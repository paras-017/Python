'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
  
print(factorial(3))    
'''

'''
Quick quiz: write a program to print the Fibonacci sequence
#ex-->0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
index  = 0
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers


'''

def series(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else: 
        return series(n-1)+series(n-2)
  
print(series(6))   
