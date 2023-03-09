tuple1 = (0,5,3,8,3,2,3,10,11,6)
print(tuple1.count(3))
print(tuple1.index(3))
print(tuple1.index(3,3,7))   #last 2 argument used for finding in between index3 to index 7-1
print(len(tuple1))


tuple2 = (1,2,3,4,6,6,7,8,9)
temp = list(tuple2)
temp[4] = 5
tuple2 = tuple(temp)
print(tuple2)

