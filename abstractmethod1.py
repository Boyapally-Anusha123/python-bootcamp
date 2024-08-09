class Employee:
    def __init__(self):
        self.name='anusha'
        self.role='developer'
        self.__salary=85000
    def get_salary(self):
        return self.__salary
    def display(self):
        print(self.name,self.role)
e1=Employee()
e1.display()
print(e1.get_salary())
