class abc:
    def display(self, name=''):
        print("This is" + name)

a = abc()
a.display()
a.display("Hardee")

class abcd:
    def display1(self):
        print("This is 2nd sentence")
class abcde(abcd): 
    def display1(self):
        super().display1()
        print("This is second sentence")

a1 = abcde()
a1.display1()


