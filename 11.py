price = int(input("Enter the integer price: "))
if (price<3000 or price>7000):
    raise ValueError("Please enter integer less than 3000")