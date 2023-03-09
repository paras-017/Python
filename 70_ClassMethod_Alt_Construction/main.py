class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    @classmethod 
    def fromStr(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])
    
    
e1 = Employee('harry',15000)
print(e1.name,e1.salary)


string = "John-12000"
e2 = Employee(string.split('-')[0], string.split('-')[1])
print(e2.name,e2.salary)

string2 = 'boby-10000'
e3 = Employee.fromStr(string2)
print(e3.name,e3.salary)



    
    
    
    
    
    
    
    
    
    
    
    
    
