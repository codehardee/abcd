class user:
    def __init__(self, name, id):
        self.name = name
        self.id = id
a = user("hardee", 21)
print(a.__dict__)
print(help(user))
b = (1,2,3,4)
dir(b)