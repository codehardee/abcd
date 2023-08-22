class emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls, string):
        name, salary = string.split("-")
        return cls(name, int(salary))  # Create an instance of the class with extracted values

a = emp("hardee", 10)
print(a.name)
print(a.salary)

string = "hardy-12000"
b = emp.fromstr(string)
print(b.name)
print(b.salary)
