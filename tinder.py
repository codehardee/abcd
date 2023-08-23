

f = str(input("Enter your first name: "))
l = str(input("Enter your last name: "))
#code1
print("Hello " + f +" "+ l)
print("Welcome to Tinder india!")
#code2

#exception handling
try:
  age = int(input("What is your age? "))
except ValueError:
  print("You should enter a number as your age! otherwise error will occur")
 
#exception example 2
try:
  if age < 18:
    raise ValueError
except ValueError:
  print("Our terms and conditions tells to not use the app, as you are under the minor category!")
  
#another age related code
for i in range(1, 100):
  if age < 18:
    print("You are not eligible to use this app!")
    break
#gender thing
print("Enter Your Gender!")
genlist = ["M", "F", "Other"]
gen = str(input(""))
gen2 = gen.split() 

#function definition
#male function
#male profile

class user:
  def __init__(self, name, occupation, hobby, age, gender):
    self.name = name
    self.occupation = occupation
    self.hobby = hobby
    self.age = age
    self.gender = gender
    print("Hiiiii")

  def info(self):
    print(f" {self.name} \n {self.occupation} \n {self.hobby} \n {self.age} \n {self.gender}")

a1 = user("hardee", "Product Manager", "Dance", "21", "Female")
a1.info()

def profile(fname, lname, age, location, hobby, emoji):
  print("Profiles that you should look at: " + fname, lname, age, location, hobby, emoji)

#female profile
def profile2(fname, lname, age, location, hobby, emoji):
  print("Profiles that you should look at: " + fname, lname, age, location, hobby, emoji)
  

if "F" in gen2:
  print("Your Welcome Miss " + f)
  print("We will show you some profiles!")
  
  profile("Leonardo", "Dicaprio","26", "Texas", "Boxing","🫠")
  profile("Kim", "Mingyu","24", "Seoul", "Dancing","🤩")
  profile("Michele", "Morrone","34", "Italy", "Modeling", "😇")
  profile("Paul", "Walker","38", "Las Vegas", "Acting", "😍")
elif "M" in gen2:
  print("Your Welcome Mister " + f)
  print("We will show you some profiles!")
  
  profile2("Taylor", "Swift","29", "New Jersey", "Singing", "😂")
  profile2("Selena", "Gomez","24", "Toronto", "Boxing", "🙃")
  profile2("Millie", "Bobby Brown","21", "Calgary", "Acting", "🥹")
  profile2("Jennie", "Kim","20", "Seoul", "Dancing", "😲")
else:
  print("Please enter your gender!")

