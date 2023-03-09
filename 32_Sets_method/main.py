s1 = {1,6,8,3,7}
s2= {2,4,5,6,7}

# Union  and Update --> The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set. 
'''
s3 = s1.union(s2)                   #S1 and s2 will be untouched(no change)
print(s3) 

s1.update(s2)               #s11 will be change
print(s1)
'''

# ________________________________________________________________________________________________________________________________________

#intersection and intersection_update():The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

'''
s3 = s1.intersection(s2)         #only common value will get
print(s3)
s1.intersection_update(s2)      #only common value will get 
print(s1)                     
'''



# ________________________________________________________________________________________________________________________________________
# symmetric_difference and symmetric_difference_update():The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
'''
s3= s1.symmetric_difference(s2)    #common will get removed
print(s3)
'''




#difference() and difference_update():The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
'''
s3= s1.difference(s2) # s1-s2
s1.difference_update(s2) # s1-s2
print(s3)
'''
