class user:
    def __init__(self):
        self._energy = None
    @property
    def energy(self):
        return self._energy
    @energy.setter
    def my_att(self,point):
        if point < 0:
            print("Value cannot be negative.")
        else:
            self._energy = point
    @energy.deleter
    def energy(self):
        print("Deleting my_attribute...")
        del self._energy

a = user()
print(a.energy)
a.energy = 42
print(a.energy)
a.energy = -42
del a.energy
print(a.energy) 


