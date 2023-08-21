with open('txtfile2', 'r') as f:
    print(type(f))

    f.seek(7)
    data = f.read(5)
    print(data)
    print(f.tell())