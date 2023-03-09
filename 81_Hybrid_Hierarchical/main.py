class Epmloyee:
    def __init__(self, name, age ,category):
        self.name = name
        self.age = age
        self.category = category
    
    def show(self):
        print(f'{self.name} age is {self.age} and belongs to {self.category} category')

        