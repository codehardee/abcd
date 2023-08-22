
class pizza:
  price = "20$"

class margherita(pizza):
  def show(self):
    print("Margherita pizza with price of ", self.price)

class cheeseburstmargherita(margherita):
    def show2(self):
      print("This is cheese burst margherita with price of ", self.price)

a = cheeseburstmargherita()
a.show2()
a.show()
b=margherita()
b.show()

