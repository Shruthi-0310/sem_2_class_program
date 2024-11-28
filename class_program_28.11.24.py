#1
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the id:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name)

class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary=",self.sal)

empl=Perks()
empl.getDetails()
empl.displayInfo()

#2
class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

class Perks(Inventory):
    def getDetails(self):
        self.getInventoryInfo()
        self.price=int(input("Enter the price: "))
    def displayInfo(self):
        self.displayInventoryInfo()
        print("Price = ",self.price)

p=Perks()
p.getDetails()
p.displayInfo()

#3
class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

p=Inventory()
p.getDetails()
p.displayInfo()
