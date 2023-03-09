lst =  [1,2,3,4,5,6,7,8,9,10]

# map
mapLst1 = list(map(lambda x:x*2, lst))
print(mapLst1)

#filter 
filterLst2 = list(filter(lambda x:x%2==0, lst))
print(filterLst2)

#reduce
from  functools import reduce
reduceLst = reduce(lambda x, y: x+y, lst)
print(reduceLst)
