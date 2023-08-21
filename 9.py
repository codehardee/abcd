info = {'name':'Karan', 'age':19, 'eligible':True, 'id':2}
print(info)
print(info['name'])
print(info.get('name'))
print(info.values)
print(info.items)
print(info.update({'age': 21}))
print(info.pop('eligible'))
print(info.popitem())
del info['age']