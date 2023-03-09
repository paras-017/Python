'''
class ParentClass:
    def parent_method(self):
        print("This is parent method" )

class ChildClass(ParentClass):
    def parent_method(self):
        print('harry')
        super().parent_method()
 
    def child_method(self):
        print("This is child method" )
        super().parent_method()
       
childObj = ChildClass() 
childObj.child_method()
childObj.parent_method()

'''



class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name , id, lang):
        super().__init__(name, id)
        self.lang = lang
       

rohan = Employee('Rohan', '420')
print(rohan.name)
print(rohan.id)
paras = Programmer('Paras', '421','javascript')
print(paras.name)
print(paras.id)
print(paras.lang)
 