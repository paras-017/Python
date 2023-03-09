import time

timestamp = int(time.strftime('%H'))
print(timestamp)
if(timestamp<12):
    print('good Morning')
elif(timestamp>=12 and timestamp<=16):
    print('good Afternoon')
else:
    print('good Evening')
    
    
    
    
    
    
    
    