class employee:
    company_name = "TechCorp"
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def sum(a, b):
        return a + b
    def print_company_name(self):
        print(f"Company Name: {self.company_name}")
    @classmethod
    def set_company_name(cls,new_name):
        cls.company_name = new_name

    @classmethod
    def get_company_name(cls):
        return cls.company_name
        #e=employee.sum(5,23)
#print(e)
print(employee.get_company_name())
employee.set_company_name("HP")
print(employee.get_company_name())