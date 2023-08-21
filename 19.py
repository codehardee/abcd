class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def func1(self):
        print(f"This is function details: {self.name} and {self.id}")
    

class EmployeeC(Employee):
    def func2(self):
        print("this is child function")
    
a = Employee("hardee", 4)
a.func1()
b = EmployeeC("Hardi", 1)
b.func1()
b.func2()