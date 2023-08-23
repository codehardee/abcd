# # # class Character:
# # #     def __init__(self, name, health):
# # #         self.name = name
# # #         self.health = health
# # #         # self.character = character
# # #     def attack(self, target):
# # #         print(f"{self.name} attacks {self.target}")
# # #         target.take_damage(self.damage)
# # #     def take_damage(self, amount):
# # #         self.health = amount
# # #         if self.health <= 0:
# # #             print(f"{self.name} has been defeated.")

# # # class Player(Character):
# # #     def __init__(self, name):
# # #         super().__init__(name, health=100)
# # #         print(f"Welcome, {self.name} , {self.health}")
# # #     def player_method(self):
# # #         type = str(input("Do you want to attack or flee?"))
# # #         print(type)
# # #         if type == "attack":
# # #             self.health -= 5
# # #             print(self.health)
# # #         else:
# # #             self.health += 5

       
# # # player_name = str(input("Enter your character name -"))
# # # a = Player(player_name)

# # # a.player_method()

# # # class Enemy(Character, ):
# # #     def enemy_method(self, enemy_name, health=100):
# # #         self.enemy_name = "Goblin"
# # #     def decrease_health(self, type):
# # #         if type == "attack":
# # #             self.health -= 10
# # #             print(self.health)

# # class Character:
# #     def __init__(self, name, health):
# #         self.name = name
# #         self.health = health
    
# #     def attack(self, target):
# #         print(f"{self.name} attacks {target.name}")
# #         target.take_damage(self.damage)
    
# #     def take_damage(self, amount):
# #         self.health -= amount
# #         if self.health <= 0:
# #             print(f"{self.name} has been defeated.")

# # class Player(Character):
# #     def __init__(self, name):
# #         super().__init__(name, health=100)
# #         print(f"Welcome, {self.name}, {self.health}")
        
# #     def player_method(self):
# #         action = input("Do you want to attack or flee?")
# #         print(action)
# #         if action == "attack":
# #             self.attack(self)  # You can call the attack method of the superclass

# # player_name = input("Enter your character name: ")
# # player = Player(player_name)

# # player.player_method()

# # class Enemy(Character):
# #     def __init__(self, name, health=100):
# #         super().__init__(name, health)
# #         self.enemy_name = name
    
# #     def enemy_method(self):
# #         print(f"{self.enemy_name} performs an enemy action.")
        
# #     def decrease_health(self, damage):
# #         self.health -= damage
# #         if self.health <= 0:
# #             print(f"{self.enemy_name} has been defeated.")

# # enemy_name = input("Enter the enemy name: ")
# # enemy = Enemy(enemy_name)

# # enemy.decrease_health(10)  # Simulate an attack on the enemy

# # if enemy.health <= 0:
# #     print(f"{enemy.enemy_name} has been defeated.")

# # if player.health <= 0:
# #     print(f"{player.name} has been defeated.")
  
# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
    
#     def attack(self, target):
#         print(f"{self.name} attacks {target.name}")
#         target.take_damage(10)  # Assume a fixed damage for simplicity
    
#     def take_damage(self, amount):
#         self.health -= amount
#         if self.health <= 0:
#             print(f"{self.name} has been defeated.")

# class Player(Character):
#     def __init__(self, name):
#         super().__init__(name, health=100)
#         print(f"Welcome, {self.name}, {self.health}")
        
#     def player_method(self):
#         action = input("Do you want to attack or flee?")
#         print(action)
#         if action == "attack":
#             self.attack(self)  # You can call the attack method of the superclass

# class Enemy(Character):
#     def __init__(self, name):
#         super().__init__(name, health=50)
#         self.enemy_name = name
    
#     def enemy_method(self):
#         print(f"{self.enemy_name} performs an enemy action.")
#     def enemy_method(self):
#         print("f{self.enemy_name} performs an enemy action.")
#     def __init__(self,enemy_name):
#         self.enemy_health
    
        
#     def decrease_health(self, damage):
#         self.health -= damage
#         if self.health <= 0:
#             print(f"{self.enemy_name} has been defeated.")

# # Creating instances of Player and Enemy
# player_name = input("Enter your character name: ")
# player = Player(player_name)

# enemy_name = input("Enter the enemy name: ")
# enemy = Enemy(enemy_name)

# # Player's action
# player.player_method()

# # Enemy's action
# enemy.decrease_health(10)  # Simulate an attack on the enemy

# # Checking defeat conditions
# if enemy.health <= 0:
#     print(f"{enemy.enemy_name} has been defeated.")

# if player.health <= 0:
#     print(f"{player.name} has been defeated.")
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        target.take_damage(10)  # Assume a fixed damage for simplicity
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100)
        print(f"Welcome, {self.name}, {self.health}")
        
    def player_method(self):
        action = input("Do you want to attack or flee?")
        print(action)
        if action == "attack":
            self.attack(self)  # You can call the attack method of the superclass
    def is_defeated(self):
        return self.health <= 0

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=50)
        self.enemy_name = name
    
    def enemy_method(self):
        print(f"{self.enemy_name} performs an enemy action.")
        
    def decrease_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.enemy_name} has been defeated.")

    def is_defeated(self):
        return self.health <= 0

# Creating instances of Player and Enemy
player_name = input("Enter your character name: ")
player = Player(player_name)

enemy_name = input("Enter the enemy name: ")
enemy = Enemy(enemy_name)

# Player's action
player.player_method()

# Enemy's action
enemy.decrease_health(10)  # Simulate an attack on the enemy

# Determining the winner
if enemy.is_defeated():
    print(f"{enemy.enemy_name} has been defeated. {player.name} wins!")
elif player.is_defeated():
    print(f"{player.name} has been defeated. {enemy.enemy_name} wins!")
else:
    print("The battle continues...")




