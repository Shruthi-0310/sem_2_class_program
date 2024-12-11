###1
##class Student:
##    __id=45  #__ is private and it will show an attribute error
##    def __init__(self,name):
##        self.__name=name
##    def display(self):
##        print("Name=",self.__name)
##s=Student("Shru")
##s.display()
##print(s.id)
##
###2
##class Student:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def displayStudentInfo(self):
##        print("Name=",self.name,"\nAge=",self.age)
##
##name=input("Name:")
##age=int(input("Age:"))
##s=Student(name,age)
##s.displayStudentInfo()
##        
###3
##class Employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.__salary=salary
##
##name=input("Name=")
##salary=int(input("Salary="))
##emp=Employee(name,salary)
##print("Name=",emp.name)
##print("Salary=",emp._Employee__salary)

###4
##
##class Employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.__salary=salary
##
##    def displayEmployeeInfo(self):
##        print(f"Employee Name=",self.name,"\nSalary=",self.salary)
##
##class TL(Employee):
##    def __init__(self,name,salary,role,teamsize):
##        super().__init__(name,salary)
##        self.role=role
##        self.teamsize=teamsize
##    def displayTLInfo(self):
##        self.displayEmployeeInfo()
##        print(f"Role=",self.role,"\nTeam Size=",self.teamsize)
##
##name=input("Name=")
##salary=int(input("Salary="))
##role=input("Role=")
##teamsize=int(input("teamsize="))
##emp=TL(name,salary,role,teamsize)
##print("Name=",emp.name)
##print("Salary=",emp._Employee__salary)
##print("Role=",emp.role)
##print("Teamsize=",emp.teamsize)

