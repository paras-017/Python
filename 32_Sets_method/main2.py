s1={1,3,5,6,7}
s2={2,4,5,6,8}
s3={11,12,13}
s4={5,6}


# isdisjoint():This method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
'''
print(s1.isdisjoint(s2))  #false        itersection h
print(s1.isdisjoint(s3))  #true         itersection nahi h
'''




# issuperset():This method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
'''
print(s2.issuperset(s4)) 
'''



# issubset():this method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
'''
print(s4.issubset(s2))
'''



# Add - to add one item
'''
s4.add(1000)
print(s4)
'''



# update- If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
'''
s5={1000,1002,1001}
s4.update(s5)
print(s4)
'''




# remove()/discard()--> We can use remove() and discard() methods to remove items form list.The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
''''
s1.remove(16)  #below code will not execute if 16 is not present but if we use discard then it will not raise an error
print(s1)

s1.discard(16)
print(s1)
'''



# pop()-->This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
'''
mySet = s1.pop()
print(s1)
print(mySet)

'''



# del-->this is not a method, rather it is a keyword which deletes the set entirely.
'''
del s4
print(s4)
'''


# clear():This method clears all items in the set and prints an empty set.
s4.clear()
print(s4)