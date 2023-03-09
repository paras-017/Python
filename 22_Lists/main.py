'''
l = [3,5,6,18,19]
print(l[-2])  #If theres a -ve  make the index positve by (length  +(-ve) index)
print(l[5-2]) 
print(l[4])
print(l)
print(l[1:-1:2])
if '6' in l:
    print('I found it')
else:
    print('I didnt find it')
    
myStr = 'This is paras string'
if "ing" in myStr:
    print('yes')
else:
    print('I didnt find it')
'''

lst = [i*i for i in range(11) if i%2 == 0]

print(lst[1:])
print(lst[-1])
print(lst[-2])
