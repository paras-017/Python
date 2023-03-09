# Set-->we create sets by placing all the elements inside curly braces {} , separated by comma. A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements and when we print set it will not print in fixed patterns like set = {1,2,3,4} ==> output->  3,2,4,1 or 4,1,2,3 ......
mySets3 = {2,5,True,'Sigma',{'Legend',True,45}}
print(mySets3) #gives erro

s={2,42,6,4,2,2}
print(s)
info = {'caral', 19, False,5.9,19}
print(info)
for value in info:
    print(value)
    
    
newSet = set({2,'car','2',90, True})  
print(newSet)

info10= {'car',45,True}
info11= {'car',45,True,False, 'parrot',22}
info12= {'car',45,False, 'parrot',22,True}
info13= {'car',45,True}
print(info10)
print(info11)
print(info12)
print(info13)


print('')



r