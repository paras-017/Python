class Employee:
    def __init__(self, em_Name, em_Id, em_language):
        self.name = em_Name
        self.id = em_Id
        self.language = em_language
     
    def showDetails(self):    
        print(f'The name of the employee is {self.name} and id is {self.id}')

class Programmer(Employee):
    def em_Detail(self):
        print(f'the employee {self.name} language is {self.language}')
        

# e1 = Employee('Paras', 'a280123','React')
# e1.showDetails()

e2 = Programmer('Harry', 'b280123', 'Javascript')
# e2.showDetails()
e2.em_Detail()


