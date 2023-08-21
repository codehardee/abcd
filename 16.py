class employee:
    def __init__(self, name, id, lname):
        self.name = name
        self.id = id
        self.lname = lname
        print("this is simple statement")
    def info(self):
        print(f"{self.name} and {self.lname}")
    # def empfunc(self):
    #     print(f"{self.name} and lastname is {self.lname} and id is {self.id}")

a = employee("Hardee", 21, "Raval")

# a.empfunc()
a.info()

b = employee("heet", 22, "Raval")
b.info()
# b.empfunc()

class peep:
    def __init__(self, *name):
        self.name = name
        
        print("this is simple statement")
    def info(self):
        for i in self.name:
            print(f"{i}")

c = peep("hardee", "heet", "xyz", "abc")
c.info()

class stud:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        # self.values = values
        print("this is simple statement")
    def dictfunc(self):
        for key, value in self.kwargs.items():
        # for i in self.kwargs:
            # print(f"key: {key}, values: {values}")
            print(f"Key: {key}, Value: {value}")

d = stud(har="raval", hit="raval", xyz="abc")
d.dictfunc()

