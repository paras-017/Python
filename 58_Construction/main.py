'''
class Person:
    name = 'paras'
    age = 18
    def info(self):
        print(f'{self.name} age is {self.age}')

a = Person()        
a.name = 'Sheik Hasina'
a.age = '8 month'
a.info()

b = Person();
b.name = 'Raju Rastogi'
b.age = '21'
b.info()
'''

class Person:
    def __init__(self,name,age):
        print(self)
        self.name = name
        self.age = age
    
    def info(self):    
        print(f'{self.name} age is {self.age}')

# a = Person('Paras', 18)
# a.info()

# b = Person('Raju Rastogi', 21)
# b.info()

# c = Person('Sheik Hasina', '8 month')
# c.info()








