class Student:
    #static data
    branch='CSE'
    def __init__(self,name,rollno,address,email):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.email=email
    def dis(self):
        print('Name is: ',self.name)
        print('Rollno  is: ',self.rollno)
        print('Branch is: ',Student.branch)
        print('Address is: ',self.address)
        print('Email is: ',self.email)
s1=Student('anu',504,'nlg','anu@gmail.com')
s2=Student('akhi',505,'nlg','akhi@gmail.com')
s1.dis()
s2.dis()
