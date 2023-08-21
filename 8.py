set1 = {"name", 2, False, "2.0"}
print(set1)
for i in set1:
    print(i)

set2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set3 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
set4 = set3.update(set2)
set5 = set3.union(set4)