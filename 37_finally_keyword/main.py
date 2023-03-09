# Finally Keyword: it will always executed for ex: in funct1 we are returning 0 and 1 for try and catch respectively but if i use print('somthing') then i will not get the value so in order to get the value we can use FINALLY keyword 

def func1():
    try:
        l = [1,5,6,7]
        i = int(input('Enter a number \n'))
        print(l[i])
        return 0
    except:
        print('Invalid input')   
        return 1
        
    finally:
             print('I am always executed')    
    # print('I am always executed')    

x = func1()    
print(x)



   