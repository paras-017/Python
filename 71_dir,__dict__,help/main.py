'''
a = [2,5,6]
print(dir(a))                       #print all method available for a
print(a.__dir__)
'''

'''
'''
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

p = Person("John",30)
print(p.__dict__)


# print(help(Person))