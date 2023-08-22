
class store:
    def __init__(self, name):
        self.name = name
    def storemethod(self):
       print("This is ", self.name)

class storetype:
    def __init__(self, type):
        self.type = type
    def storemethod(self):
       print("This is", self.type, "store")

class storetypestore(store, storetype):
   def __init__(self, type, name):
      self.type = type
      self.name = name
    
a = store("seven-eleven")
a.storemethod()

b = storetype("online")
b.storemethod()

c = storetypestore("seveneleven", "seveneleven-offline")
c.storemethod()