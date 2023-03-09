class Employee:
    def __init__(self, name, lang):
        self.__name = name
        self.__lang = lang

    def info(self):
        print(f"{self.__name} favourite language is {self.__lang}")

a = Employee('Paras','javascript')
print(a._Employee__name)
a.info()


