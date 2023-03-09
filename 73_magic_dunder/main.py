class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i
        
    def __str__(self):   
        return f"The name of the employee {self.name} str"

    def __repr__(self):                      #This method tells the way we can  recreate this object we can write anything in this -->  lyrics,song
        return f"The name of the employee {self.name} repr"

    def __call__(self):    
        return ()

