# F-String -->in Javascript we use ${variable} to use variable inside any string sentence and in python we use f-string
myName = 'paras'
myOrigin = 'India'
myAge = 18
# with using f-string  LATEST
print('my name is {myName} and I belong from country {myOrigin} my age is {age}')

# without f-string
# Method-1
sentence1= 'my name is {} and I belong from country {} my age is {}'
print(sentence1.format('paras', 'India',18))


#Method-2
sentence2 = 'my name is {1} and I belong from country {0} my age is {2}'
print(sentence2.format('paras',32, 'India'))



