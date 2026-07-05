class person():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self): #getter
        return self.__name
    @name.setter
    def name(self, new_name): #setter
        self.__name = new_name
p = person("John")
print(p.name)
p.name = "Doe"
print(p.name)