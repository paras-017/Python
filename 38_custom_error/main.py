a = input('Enter any number value between 5 and 9 or enter quit \n')
try:
    if(int(a) <5 or int(a) > 9):
        raise ValueError("Invalid number")
except:
    if a!=  'quit':    
        raise ValueError("Invalid string")