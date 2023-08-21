sqr = lambda x:x*x
print(sqr(5))

#map, filter, reduce

def cube(y):
    return y*y*y
lst = [1,2,3,4,5,6]
newlist = list(map(cube,lst))
print(newlist)

list2=list(map(lambda z:z*z*z, lst))
print(list2)

list3 = [1,2,3,4,5,6,7]
def func1(a):
    return a<5
newlist = list(filter(func1,list3))
print(newlist)

from functools import reduce
numbers = [1,2,3,4,5,6]
def mysum(c, d):
    return c+d
sum = reduce(mysum,numbers)
print(sum)
print(type(sum))