class Student:
    #static data
    branch='CSE'
    def __init__(self,name,rollno,address,email):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name},{self.rollno},{Student.branch}, {self.address},{self.email}'
s1=Student('anu',504,'nlg','anu@gmail.com')
s2=Student('akhi',505,'nlg','akhi@gmail.com')
print(s1)
print(s2)
