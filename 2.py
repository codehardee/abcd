x = int(input("enter the number:"))

match x:
    case 0:
        print("its zero")
    case 10:
        print("its match")
    case _ if x!= 90:
        print("sorry")