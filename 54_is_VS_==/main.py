# is--> is compare  exact location in the memory 
# == -->  it compare values  ex: a and b 
a = (1,2,3)
b =  (1,2,3)

c = [1,2,3]
d =  (1,3,2)

print(c is d) #exact location of object in memory
print(a == b)  #value