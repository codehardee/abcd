class area:
    def find_area(self, a=None, b=None):
        if a!= None and b!= None:
            print("Area of rect: ",(a*b))
        elif a!=None:
            print("area of sqr: ",(a*a))
        else:
            print("No area, blackhole!")

a = area()
a.find_area()
a.find_area(10)
a.find_area(10,20)

class cls1:
    def method1(self):
        print("This is method1")
class cls2(cls1):
    def method1(self):
        print("This is method 2")

b = cls2()
b.method1()
