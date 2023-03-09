import random
import string

Message = input('Enter a secret message\n').split()
arr = []
secretCodeMessage = ' '
for i in range(0, len(Message)):
    if(len(Message[i])<=2):
        # print(Message[i][::-1])
        arr.append(Message[i][::-1])
    elif(len(Message[i])>=3):
        # print(f"{''.join(random.sample(string.ascii_lowercase, k=3))}{Message[i]}{''.join(random.sample(string.ascii_lowercase, k=3))}")    
        arr.append(f"{''.join(random.sample(string.ascii_lowercase, k=3))}{Message[i]}{''.join(random.sample(string.ascii_lowercase, k=3))}")
        
        
print(secretCodeMessage.join(arr))        

# print()