class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary # private data
    def get_salary(self):    # public method nd data is private
        return self.__salary
    def Empdisplay(self):    #public method
        print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self): #protected method
        print("hiring for the manage role")
cobj=Company('wipro','gachibowli')
eobj=Employee('umer','dev',85000)
eobj.Empdisplay()
print(cobj._hiring())
