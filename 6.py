numbers = [1,2,2,2,3,4]
numbers.sort(reverse=True)
print(numbers)
print(numbers.index(2))
print(numbers.count(2))
numbers2 = numbers.copy()
print(numbers.append(5))
numbers.extend(numbers2)
print(numbers)

numlist = numbers+ numbers2
print(numlist)