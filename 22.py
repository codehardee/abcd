class user:
    def __init__(self):
        self.__name = "Hardee"
a = user()
print(a._user__name)

class user2:
    def __init__(self):
        self._name = "Hardee"
    def _func1(self):
        return "codewithhardee"
    
class user3(user2):
    pass
 
a1 = user3()
a2 = user3()
print(a1._name)
print(a1._func1())
print(a2._name)
print(a2._func1())
