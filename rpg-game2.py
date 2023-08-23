class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage.")
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, damage=10)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You found {item}!")

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def drop_loot(self):
        return f"{self.name}'s sword"

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    enemy = Enemy("Goblin", health=30, damage=5)

    print(f"Welcome, {player.name}! You are on an adventure.")
    print("You encounter a goblin!")

    while player.health > 0 and enemy.health > 0:
        action = input("Do you want to attack or flee? ")
        if action == "attack":
            player.attack(enemy)
            if enemy.health > 0:
                enemy.attack(player)
        elif action == "flee":
            print("You fled from the battle.")
            break

    if player.health > 0:
        loot = enemy.drop_loot()
        player.add_item(loot)
        print(f"You defeated the {enemy.name} and obtained {loot}!")
    else:
        print("Game Over. You were defeated.")

if __name__ == "__main__":
    main()
