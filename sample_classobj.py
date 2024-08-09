class Student:
    def __init__(self,name,rollno,branch,address,email):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.address=address
        self.email=email
    def dis(self):
        print('Name is: ',self.name)
        print('Rollno  is: ',self.rollno)
        print('Branch is: ',self.branch)
        print('Address is: ',self.address)
        print('Email is: ',self.email)
s1=Student('anu',504,'cse','nlg','anu@gmail.com')
s1.dis()
