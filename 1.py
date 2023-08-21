str1 = "Hardee"
str2 = 'Hardee,  "Raval'
str3 = '''Hardee,  "Raval"'''
print(str1)
print(str2)
print(str3)
for i in str1:
    print(i)

print(str1[0:6])
print(str1[:])
print(str1[:-3])
print(str1[-1:])

print(str1.upper())
print(str1.lower())

str4 = "hardee   !!!     raval"
print(str4.rstrip("!"))
print(str4.replace("har", "dar"))
print(str4.split(" "))
print(str1.center(50))