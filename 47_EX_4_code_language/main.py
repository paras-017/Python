#  my name is paras --> ym qwtenamabc si poisparaqwe
# Encode or Decode

import random
import string

def getRandomString():
    letters = string.ascii_lowercase 
    result = ''.join(random.choice(letters) for i in range(3))
    return result

# getRandomString()

choice = input('press "E" for Encode or "D" for Decode \n')
m = input('Enter a message:\n')
msg = m.split(' ')

       

def encode():
    temp = []
    for word in msg:
        if(len(word)<=2):
            temp.append(word[::-1])
        else:
            sCode = getRandomString() +  word[1:] + word[0] + getRandomString()   
            temp.append(sCode)
    print(" ".join(temp))        
    
# encode()

def decode():
    temp = []
    for word in msg:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            temp.append(stnew)
        else:
            temp.append(word[::-1])    
    print(" ".join(temp))        

# decode()
if(choice == 'E'):
    encode()
else:
    decode()