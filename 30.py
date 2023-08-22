# foods = list()
# while(food := input("what would you like to have?")) != "quit":
#     foods.append(food)
#     print("okay will provide you!", foods)

# import sys

# foods = list()
# while (food := input("what would you like to have?")) != "quit":
#     foods.append(food)
#     print("okay will provide you!", foods)
#     sys.stdout.flush()

foods = list()
while (food := input("What food do you like?: ")) != "quit":
  foods.append(food)

print(foods)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

