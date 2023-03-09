# instance variables -->we use IV when we have to associate property to particular Object
class Employee:                                    
     companyName = 'Apple'
     def __init__(self, name, salary):
        self.name = name
        self.salary = salary
     def showDetail(self):
        print(f'The Employee {self.name} salary is {self.salary} in company {self.companyName}')

emp1 = Employee('Paras','4000000',)        
emp1.companyName = 'Blocks'
emp1.showDetail()

emp2 = Employee('Satyam','100000',)        
emp2.showDetail()