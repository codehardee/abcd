class parentcls:
    def parent_method(self):
        print("this is parent method")
class childclass(parentcls):
    def child_method(self):
        print("this is child method")
        super().parent_method()
a = childclass()
a.child_method()

class parentclass1:
    def parentmeth(self):
        print("number-1")
class parentclass2:
    def parentmeth1(self):
        print("number-2")
class childclass1(parentclass1,parentclass2):
    def childmeth(self):
        print("number-3")
        super().parentmeth()
        super().parentmeth1()
b = childclass1()
b.childmeth()