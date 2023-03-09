# String Immutable -- can't be changed
a = 'Harry!!!!!!! hello my name is Khan'
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","Paras"))
print(a.split())
print(a.replace("Paras", 'ducati'))
print(a.split(' '))

b = 'introduction to jS'    #first word to uppercase and rest to lowercase
print(b.capitalize())
print(b.center(100))
print(a.count('a'))
print(a.endswith('n'))
print(a.find('hello')) #returns first occurence index and if not founded it return -1
print(a.index('hello'))  #returns index of first occurence and error if not found

c = 'password123'
# print(c.isalnum())

d = 'passWorErd'
# print(d.isalpha())
# print(c.islower())

e = 'Is Capitalize True Or Not'
print(e.istitle())
print(e.swapcase())     # lower to capital and capital to lower

f = 'my name is paras'
print(f.title()) #first word of every letter to uppercase



