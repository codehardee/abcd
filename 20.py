from abc import ABC, abstractmethod

class user(ABC):
    @abstractmethod
    def userprop(self):
        pass

class citizen(user):
    def __init__(self, username, id, energy):
        self.username = username
        self.id = id
        self.energy = energy
    def userprop(self):
        print(f"energy of this citizen is {self.energy}")

class enemy(user):
    def __init__(self, team, id, energy):
        self.team = team
        self.id = id
        self.energy = energy
    def userprop(self):
        print(f"From team: {self.team} and energy is: {self.energy}")
    
# a = citizen("hardee", 21, 99)
# a.userprop()

citizen_name = input("Enter citizen's username: ")
citizen_id = int(input("Enter citizen's ID: "))
citizen_energy = int(input("Enter citizen's energy: "))
a = citizen(citizen_name, citizen_id, citizen_energy)
a.userprop()

# b = enemy("hardi", 22, 199)
# b.userprop()

enemy_team = input("Enter enemy's team: ")
enemy_id = int(input("Enter enemy's ID: "))
enemy_energy = int(input("Enter enemy's energy: "))
b = enemy(enemy_team, enemy_id, enemy_energy)
b.userprop()