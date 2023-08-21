def func1(a):
    square = a*a
    print(square)

b = 2
func1(b)

#default arg
def func2(a, b=2, c=3):
    print("number is", a,b,c)
func2(a=4)

#keyword
def func3(d, e):
    print("number is",e,d)
func3(d=10,e=11)

#variable
#i.arbitrary
def fruits(*name):
  print("My fav fruits are", name[0], name[1], name[2])
fruits("Avocado", "berry", "strawberry")


#2.keyword arbitrary
def name(**name):
  print("It's ", name["fname"], name["lname"])
name(fname="Hardee", lname="Raval")

#imp* return statement
def name(fname, sname, lname):
  return("It's " + fname +" "+sname+" "+lname)
print(name("Hardee", "Billioniare", "Raval"))