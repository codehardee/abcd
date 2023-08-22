
# class Vector:
#   def __init__(self, i, j, k):
#     self.i = i
#     self.j = j
#     self.k = k



#     def __str__(self):
#        return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self, x):
#        return Vector(self.i + x.i, self.j +x.j, self.k+x.k)

# a = Vector(1,2,3)
# print(a)

# b = Vector(4,5,6)
# print(b)

# print(a + b)
# print(type(a+b))
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            raise ValueError("Can only add Vector objects")
    
    def __str__(self):
        return f"({self.x}, {self.y})"

a = Vector(1, 2)
b = Vector(3, 4)
c = a + b
print(c)
