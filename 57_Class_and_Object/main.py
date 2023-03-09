class employee:
    name = "Default_name"
    occupation = "Default_occupation"
    networth = "$1000"
    def info(self):
        print(f'{self.name} is a {self.occupation} with a total net wroth of {self.networth}')

a = employee()        
a.name = 'paras'
a.occupation = 'Full stack developer'
a.networth = '$10000000'

a.info()


b = employee()
b.name = 'Suzie'
b.occupation = 'cat'
b.networth = 'life Time food'
b.info()